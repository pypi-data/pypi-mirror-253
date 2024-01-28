import asyncio
import json
import os
import pkgutil

import isodate
import pandas as pd
from googleapiclient.errors import HttpError

from videolab_youtube_crawler.CrawlerObject import _CrawlerObject

NUMERR_FLAG = -1
STRERR_FLAG = "unknown"
cate_data = pkgutil.get_data(__name__, "CATEGORY_US.json")
US_CATE = json.loads(cate_data.decode("utf-8"))


class VideoCrawler(_CrawlerObject):
    """Get all video_raw data"""

    def crawl_videos_in_list(self, video_list_workfile=f"DATA/list_video.csv", **kwargs):
        """
        Using video_list.csv to crawl further information. Crawled info documentation is in YouTube API.
        :keyword search_key: which search key to use to crawl in video_list.csv.
        :keyword video_id: specify which column contains video ids (ids must append ":" before the actual id).
        :return: the result will be saved in YouTube_RAW/video_data/ with one json of one video
        """
        video_column = kwargs.get('video_id', 'videoId')
        core = kwargs.get("core", 8)
        df = pd.read_csv(video_list_workfile)
        asyncio.run(self._crawl_videos_in_df(df, video_column, f"{self.data_video_json}", core))

    async def _crawl_videos_in_df(self, df, video_column, video_data_dir, core):
        # add filtering here
        coros = []
        for index, row in df.iterrows():
            video_id = row[video_column][1:]  # remove the ":" in the 1st char
            filename = video_id + ".json"
            print(f"Crawling {filename}")
            if not self._isCrawled(f"{video_data_dir}/" + filename):
                searchKey = row['searchKey'] if "searchKey" in row else ""
                coros.append(self._crawl_one_video(video_id, searchKey, video_data_dir, filename))
                if len(coros) % core == 0:
                    await asyncio.gather(*coros)
                    coros = []
            else:
                print(f"Skip {video_id}, already crawled in {video_data_dir}")
        if len(coros) > 0:
            await asyncio.gather(*coros)

    async def _crawl_one_video(self, video_id, search_key, video_data_dir, filename):
        video = self._get_video(video_id)
        if video != 'error':
            result = {
                "videoId": video_id,
                "video": video,
                "searchKey": search_key,
            }
            try:
                os.mkdir(f"{video_data_dir}/")
            except OSError:
                pass
            with open(f"{video_data_dir}/" + filename, 'w+') as fp:
                fp.write(json.dumps(result) + "\n")
        else:
            print(f'error crawling {video_id}')

    def _get_video(self, video_id):
        """
        Get one video by id
        :param video_id:
        :return:
        """
        # part = "id,snippet,statistics,contentDetails"
        # ,fileDetails,liveStreamingDetails,localizations,player,processingDetails,recordingDetails,status,suggestions,topicDetails
        part = "id,snippet,statistics,contentDetails,liveStreamingDetails,localizations,player,recordingDetails,status,topicDetails"
        try:
            response = self.youtube.videos().list(part=part,
                                                  maxResults=1,
                                                  id=video_id).execute()
            if len(response["items"]) == 0:
                return "error"
            return response["items"][0]
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._get_video(video_id)
        except Exception as e:
            print(e)
            return "error"

    def json_to_csv(self, **kwargs):
        """
        merge all collected JSONs from video_data to one file.
        :param kwargs: you can specify the source JSON folder by configure  directory={your own dir}
        you can specify the name of merged file by configure save_to={your file name}
        :return:
        """

        # search_key is either None, or a list of search keys
        video_data_directory = kwargs.get("data_video_json", f"{self.data_video_json}")
        video_save_to = f"{self.youtube_csv}videos.csv"

        try:
            os.mkdir(f"{self.youtube_csv}/")
        except OSError:
            print("Directory already exists %s" % self.youtube_csv)

        # handling finding directories
        if not os.path.isdir(video_data_directory):
            raise FileNotFoundError(f"can't find {video_data_directory}")
        else:
            json_list_dir = [file for file in os.listdir(video_data_directory) if file.endswith(".json")]
            all_videos = []
            for js in json_list_dir:
                with open(video_data_directory + js, 'r') as fp:
                    jobj = json.load(fp)
                    video = self._get_video_obj(jobj)
                    if video:
                        all_videos.append(video)
            df = pd.DataFrame(data=all_videos)
            df.to_csv(video_save_to, index=False)

    def _get_video_obj(self, data):
        if self._quick_reject(data, "video"):
            return None
        return {
            # video_info
            "searchKey": data["searchKey"],
            "embedUrl": "https://www.youtube.com/embed/{0}".format(data["video"]["id"]),
            "videoId": ":" + data["video"]["id"],
            "channelId": data["video"]["snippet"]["channelId"],
            "title": data["video"]["snippet"]["localized"]["title"],
            "tags": json.dumps(data["video"]["snippet"]["tags"]) if "tags" in data["video"]["snippet"] else "[]",
            "duration": self._get_duration(data["video"]["contentDetails"]["duration"]),
            "publishedAt": data["video"]["snippet"]["publishedAt"],
            "categoryId": data["video"]["snippet"]["categoryId"],
            "categories": self._get_video_category(data["video"]["snippet"]["categoryId"]),
            "description": data["video"]["snippet"]["localized"]["description"],
            "commentCount": int(data["video"]["statistics"]["commentCount"]) if "commentCount" in data["video"][
                "statistics"] else NUMERR_FLAG,
            "viewCount": int(data["video"]["statistics"]["viewCount"]) if "viewCount" in data["video"][
                "statistics"] else NUMERR_FLAG,
            "likeCount": int(data["video"]["statistics"]["likeCount"]) if "likeCount" in data["video"][
                "statistics"] else NUMERR_FLAG,
            "dislikeCount": int(data["video"]["statistics"]["dislikeCount"]) if "dislikeCount" in data["video"][
                "statistics"] else NUMERR_FLAG,
            "videoUrl": "https://www.youtube.com/watch?v={0}".format(data["video"]["id"]),
            "defaultAudioLanguage": data["video"]["snippet"]["defaultAudioLanguage"] if "defaultAudioLanguage" in
                                                                                        data["video"]["snippet"]
            else STRERR_FLAG,
        }

    def _quick_reject(self, data, part):
        if data[part] == "error":
            return True
        if part == "video":
            try:
                if data["video"] is None \
                        or data["video"]["snippet"] is None \
                        or data["video"]["snippet"]["localized"] is None \
                        or data["video"]["snippet"]["channelId"] is None:
                    return True
            except TypeError or KeyError:
                return True
        return False

    def _get_video_category(self, categoryId):
        categories = US_CATE
        for cate in categories:
            if cate["id"] == categoryId:
                return cate["snippet"]["title"]
        for cate in US_CATE:
            if cate["id"] == categoryId:
                return cate["snippet"]["title"]

    def _get_duration(self, duration):
        dur = isodate.parse_duration(duration)
        return dur.total_seconds()
