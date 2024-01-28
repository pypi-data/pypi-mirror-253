import asyncio
import json
import os
import pandas as pd
from googleapiclient.errors import HttpError

from videolab_youtube_crawler.CrawlerObject import _CrawlerObject

NUMERR_FLAG = -1
STRERR_FLAG = "unknown"


class CommentCrawler(_CrawlerObject):
    """Get all video_raw data"""

    def crawl_comments_of_videos(self, video_list_workfile=f"DATA/list_video.csv", comment_page=2, **kwargs):
        """
        Using video_list.csv to crawl further information. Crawled info documentation is in YouTube API.
        :keyword search_key: which search key to use to crawl in video_list.csv.
        :keyword video_id: specify which column contains video ids (ids must append ":" before the actual id).
        :return: the result will be saved in YouTube_RAW/video_data/ with one json of one video
        """
        video_column = kwargs.get('video_id', 'videoId')
        core = kwargs.get("core", 8)
        df = pd.read_csv(video_list_workfile)
        asyncio.run(self._crawl_comments_in_df(df, comment_page, video_column, f"{self.data_comment_json}", core))

    async def _crawl_comments_in_df(self, df, comment_page, video_column, comment_data_dir, core):
        # add filtering here
        coros=[]
        for index, row in df.iterrows():
            video_id = row[video_column][1:]  # remove the ":" in the 1st char
            filename = video_id + ".json"
            print(f"Crawling {filename}")
            if not self._isCrawled(f"{comment_data_dir}/" + filename):
                coros.append(self._crawl_one_video(video_id, comment_page, comment_data_dir, filename))
                if len(coros) % core == 0:
                    await asyncio.gather(*coros)
                    coros=[]
            else:
                print(f"Skip {video_id}, already crawled in {comment_data_dir}")
        if len(coros) > 0:
            await asyncio.gather(*coros)

    async def _crawl_one_video(self, video_id, comment_page_count, comment_dir, filename):

        comments = self._get_comments(video_id, comment_page_count)
        if comments != "error":
            result = {
                "videoId": video_id,
                "comments": comments
            }
            try:
                os.mkdir(f"{comment_dir}/")
            except OSError:
                pass
            with open(f"{comment_dir}/" + filename, 'w+') as fp:
                fp.write(json.dumps(result) + "\n")

    def _get_comments(self, video_id, comment_page_count):
        """
        Save video comments of all the videos saved in {channel_list_dir}
        JSON returned from https://developers.google.com/youtube/v3/docs/comments
        :param video_id:
        :param comment_page_count:
        :return:
        """
        part = "snippet"
        try:
            response = self.youtube.commentThreads().list(part=part,
                                                          maxResults=100,
                                                          videoId=video_id).execute()
            comments = response["items"]
            counter = 0  # save the first page_count pages
            while "nextPageToken" in response:
                page_token = response["nextPageToken"]
                response = self.youtube.commentThreads().list(part=part,
                                                              maxResults=100,
                                                              videoId=video_id,
                                                              pageToken=page_token).execute()
                comments += response["items"]
                if counter == comment_page_count:
                    return comments
                counter += 1
            return comments
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._get_comments(video_id, comment_page_count)
        except Exception as e:
            return "error"

    def json_to_csv(self, **kwargs):
        """
        merge all collected JSONs from video_data to one file.
        :param kwargs: you can specify the source JSON folder by configure  directory={your own dir}
        you can specify the name of merged file by configure save_to={your file name}
        :return:
        """

        # search_key is either None, or a list of search keys
        comment_data_directory = kwargs.get("data_comment_json", f"{self.data_comment_json}")
        save_to = f"{self.youtube_csv}comments.csv"

        try:
            os.mkdir(f"{self.youtube_csv}/")
        except OSError:
            print("Directory already exists %s" % self.youtube_csv)

        # handling finding directories
        if not os.path.isdir(comment_data_directory):
            raise FileNotFoundError(f"can't find {comment_data_directory}")
        else:
            json_list_dir = [file for file in os.listdir(comment_data_directory) if file.endswith(".json")]
            all_comments = []
            for js in json_list_dir:
                with open(comment_data_directory + js, 'r') as fp:
                    jobj = json.load(fp)
                    comments = self._get_comment_obj(jobj)
                    if comments:
                        all_comments.extend(comments)
            df = pd.DataFrame(data=all_comments)
            df.to_csv(save_to, index=False)

    def _get_comment_obj(self, data):
        if data["comments"] and data["comments"] != "error":
            comments = []
            for c in data["comments"]:
                comments.append({
                    "commentId": c["snippet"]["topLevelComment"]["id"] if "topLevelComment" in c[
                        "snippet"] else STRERR_FLAG,
                    "videoId": ":" + data["videoId"],
                    "authorDisplayName": c["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                    "authorChannelId": c["snippet"]["topLevelComment"]["snippet"]["authorChannelId"][
                        "value"] if "authorChannelId" in c["snippet"]["topLevelComment"][
                        "snippet"] else NUMERR_FLAG,
                    "likeCount": c["snippet"]["topLevelComment"]["snippet"]["likeCount"],
                    "publishedAt": c["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
                    "totalReplyCount": c["snippet"]["totalReplyCount"],
                    "textDisplay": c["snippet"]["topLevelComment"]["snippet"]["textDisplay"],
                })
            return comments
        else:
            return None
