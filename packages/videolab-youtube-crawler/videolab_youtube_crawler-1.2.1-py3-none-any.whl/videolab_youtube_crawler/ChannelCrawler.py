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


class ChannelCrawler(_CrawlerObject):
    """Get all video_raw data"""

    def __init__(self, region_code="US"):
        self.region_code = region_code
        super().__init__()

    def crawl_channel_of_videos(self, video_list_workfile=f"DATA/list_video.csv", **kwargs):
        """
        Using video_list.csv to crawl further information. Crawled info documentation is in YouTube API.
        :keyword search_key: which search key to use to crawl in video_list.csv.
        :keyword video_id: specify which column contains video ids (ids must append ":" before the actual id).
        :return: the result will be saved in YouTube_RAW/video_data/ with one json of one video
        """
        channel_column = kwargs.get('channel_id', 'channelId')
        core = kwargs.get("core", 8)
        df = pd.read_csv(video_list_workfile)
        df = df.groupby(by=channel_column).agg({
            'videoId': 'first',
            # 'searchKey': lambda x: json.dumps(list(x))
        })
        df = df.reset_index()
        asyncio.run(self._crawl_channels_in_df(df, channel_column, f"{self.data_channel_json}", core))

    def crawl_channel_in_list(self, channel_list_workfile='DATA/channel_list.csv', **kwargs):
        channel_column = kwargs.get('channel_id', 'channelId')
        core = kwargs.get("core", 8)
        df = pd.read_csv(channel_list_workfile)
        asyncio.run(self._crawl_channels_in_df(df, channel_column, f"{self.data_channel_json}", core))

    async def _crawl_channels_in_df(self, df, channel_column, channel_data_dir, core):
        # add filtering here
        coros = []
        for index, row in df.iterrows():
            channel_id = row[channel_column]
            filename = channel_id + ".json"
            print(f"Crawling {filename}")
            if not self._isCrawled(f"{channel_data_dir}/" + filename):
                # searchKey = row['searchKey'] if "searchKey" in row else ""
                coros.append(self._crawl_one_channel(channel_id, channel_data_dir, filename))
                if len(coros) % core == 0: # n task prepared, start crawling.
                    await asyncio.gather(*coros)
                    coros = []
            else:
                print(f"Skip {channel_id}, already crawled in {channel_data_dir}")
        if len(coros) > 0:
            await asyncio.gather(*coros)

    async def _crawl_one_channel(self, channel_id, channel_data_dir, filename):
        channel = self._get_channel(channel_id)
        if channel != 'error':
            result = {
                "channelId": channel_id,
                "channel": channel,
                # "searchKey": search_key,
            }
            try:
                os.mkdir(f"{channel_data_dir}/")
            except OSError:
                pass
            with open(f"{channel_data_dir}/" + filename, 'w+') as fp:
                fp.write(json.dumps(result) + "\n")
        else:
            print(f'error crawling {channel_id}')

    def _get_channel(self, channel_id):
        """
        # Save channel info of all the videos saved in {video_list_dir}
        :param channel_id:
        :return:
        """
        try:
            part = "id,snippet,statistics,contentDetails,topicDetails,brandingSettings,contentOwnerDetails," \
                   "localizations "
            response = self.youtube.channels().list(part=part, maxResults=1, id=channel_id).execute()
            return response["items"][0]
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._get_channel(channel_id)
        except Exception as e:
            return "error"

    def _search_channel(self, channelId, part='statistics'):
        part = part
        try:
            response = self.youtube.channels().list(
                part=part,
                id=channelId
            ).execute()
            return response
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._search_channel(channelId)
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
        channel_data_directory = kwargs.get("data_channel_json", f"{self.data_channel_json}")
        channel_save_to = f"{self.youtube_csv}channels.csv"

        try:
            os.mkdir(f"{self.youtube_csv}/")
        except OSError:
            print("Directory already exists %s" % self.youtube_csv)

        # handling finding directories
        if not os.path.isdir(channel_data_directory):
            raise FileNotFoundError(f"can't find {channel_data_directory}")
        else:
            json_list_dir = [file for file in os.listdir(channel_data_directory) if file.endswith(".json")]
            all_channels = []
            for js in json_list_dir:
                with open(channel_data_directory + js, 'r') as fp:
                    jobj = json.load(fp)
                    channel = self._get_channel_obj(jobj)
                    if channel:
                        all_channels.append(channel)
            df = pd.DataFrame(data=all_channels)
            df.to_csv(channel_save_to, index=False)

    def _get_channel_obj(self, data):
        if self._quick_reject(data, "channel"):
            return None
        return {
            "channelId": data["channel"]["id"],
            "title": data["channel"]["snippet"]["localized"]["title"],
            "description": data["channel"]["snippet"]["localized"]["description"]
            if "description" in data["channel"]["snippet"]["localized"] else STRERR_FLAG,
            "subscriberCount": int(data["channel"]["statistics"]["subscriberCount"])
            if "subscriberCount" in data["channel"]["statistics"] else NUMERR_FLAG,
            "publishedAt": data["channel"]["snippet"]["publishedAt"]
            if "publishedAt" in data["channel"]["snippet"] else STRERR_FLAG,
            "country": data["channel"]["snippet"]["country"]
            if "country" in data["channel"]["snippet"] else STRERR_FLAG,
            "videoCount": int(data["channel"]["statistics"]["videoCount"]),
            "KEYWORDVideoCount": 1,
            "viewCount": int(data["channel"]["statistics"]["viewCount"]),
            "topicCategories": json.dumps(self._get_category(data["channel"])),
        }

    def _quick_reject(self, data, part):
        if data[part] == "error":
            return True
        if part == "channel":
            try:
                if data["channel"] is None \
                        or data["channel"]["snippet"] is None \
                        or data["channel"]["id"] is None:
                    return True
            except TypeError or KeyError:
                return True
        return False

    def _get_video_category(self, channel, categoryId):
        categories = []
        if "videoCategories" not in channel:
            categories = US_CATE
        else:
            categories = channel["videoCategories"]["items"]
        for cate in categories:
            if cate["id"] == categoryId:
                return cate["snippet"]["title"]
        for cate in US_CATE:
            if cate["id"] == categoryId:
                return cate["snippet"]["title"]

    def _get_category(self, channel):
        result = []
        if "topicDetails" in channel and "topicCategories" in channel["topicDetails"]:
            cate_list = channel["topicDetails"]["topicCategories"]
            for cate in cate_list:
                result.append(cate.split('/')[-1])
        return result

    def _get_duration(self, duration):
        dur = isodate.parse_duration(duration)
        return dur.total_seconds()

    def crawl_all_videos_of_channels(self, channel_list_workfile="DATA/channel_list.csv", **kwargs):
        """
        async version to crawl channels
        crawl all videos belong to a list of channels (specified by channelIds)
        :param kwargs: specify channel_header to configure which column contains channel id
        :return:
        """
        header = kwargs.get("channel_header", "channelId")
        video_data_dir = self.list_video
        core = kwargs.get("core", 5)
        df = pd.read_csv(channel_list_workfile)
        self.channel_list = list(set(df[header]))
        try:
            os.mkdir(f"{self.list_video}/")
        except OSError:
            print("Directory already exists %s" % self.list_video)
        asyncio.run(self._crawl_video_list(core, video_data_dir))

    async def _crawl_video_list(self, core, video_data_dir):
        for idx in range(0, len(self.channel_list), core):
            sublist = self.channel_list[idx:idx + core]
            await self._crawl_video_list_async(sublist, video_data_dir)

    async def _crawl_video_list_async(self, sublist, search_key_subdir):
        coros = []
        for channelId in sublist:
            dir = f"{search_key_subdir}/{channelId}.json"
            if not self._isCrawled(dir):
                print(f"Crawling a video list from {channelId}....")
                coros.append(self._search_videos_from_channels_async(dir, channelId))
            else:
                print(f"Skip {channelId}, channel already crawled")
        await asyncio.gather(*coros)

    async def _search_videos_from_channels_async(self, file_name, channel_id):
        response = self._search_all_videos_in_channel(file_name, channel_id)
        total_results = response["pageInfo"]["totalResults"]
        print(f"Total videos: {total_results}")
        while response is not None and "nextPageToken" in response:
            response = self._search_all_videos_in_channel(file_name, channel_id, response["nextPageToken"])

    def _search_all_videos_in_channel(self, file_path, channel_id, page_token=None):
        """
        Get all videos of a channel
        :param file_path: the directory to save the returned json
        :param channel_id:
        :param page_token:
        :return:
        """
        part = "snippet"
        try:
            if page_token:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      pageToken=page_token,
                                                      type="video",
                                                      channelId=channel_id,
                                                      regionCode=self.region_code
                                                      ).execute()
            else:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      type="video",
                                                      channelId=channel_id,
                                                      regionCode=self.region_code
                                                      ).execute()
            self._write_item(file_path, response["items"])
            return response
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._search_all_videos_in_channel(file_path, channel_id,
                                                          page_token)  # I assume it's missing one var
        except Exception as e:
            print(e)
            return "error"
