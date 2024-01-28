## Import and configuration
import json
import os
from configparser import ConfigParser
import pandas as pd
from googleapiclient.errors import HttpError
from videolab_youtube_crawler.CrawlerObject import _CrawlerObject

CONFIG = "config.ini"
config = ConfigParser(allow_no_value=True)
config.read(CONFIG)


class ChannelSearcher(_CrawlerObject):
    def __init__(self):
        super().__init__()

    def search(self, search_key, **kwargs):
        self.region_code = kwargs.get("region_code", "US")
        self.search_key = search_key

        try:
            os.mkdir(f"{self.list_channel}/")
        except OSError:
            print("Directory already exists %s" % self.list_channel)

        save_to = f"{self.list_channel}{self._get_search_short(self.search_key)}.json"
        if not os.path.exists(save_to):
            self._crawl_channels(save_to)
        else:
            print(f'{save_to} existed. Skip search key {search_key}')

    def _crawl_channels(self, file_path):
        response = self._search_channel(file_path=file_path)
        if response != "error":
            total_result = response["pageInfo"]["totalResults"]
            if "nextPageToken" not in response:
                print(f"total results:{str(total_result)}")
                return
            while True:
                response = self._search_channel(file_path=file_path,
                                                page_token=response["nextPageToken"])
                if "nextPageToken" not in response:
                    print(f"total results:{str(total_result)}")
                    break

    def _search_channel(self, file_path, page_token=None):
        """
        Crawl a list of videos which matches {search_key}. Save the data in {video_list_dir}
        JSON returned from https://developers.google.com/youtube/v3/docs/search/list
        :param file_path: file to save the returned json
        :param page_token: A page token to start with
        :return: success or error message
        """
        part = "snippet"
        try:
            if page_token:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      q=self.search_key,
                                                      pageToken=page_token,
                                                      type="channel",
                                                      regionCode=self.region_code
                                                      ).execute()
            else:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      q=self.search_key,
                                                      type="channel",
                                                      regionCode=self.region_code
                                                      ).execute()
            self._write_item(file_path, response["items"])  # remove duplicate
            return response
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._search_channel(file_path, page_token)
        except Exception as e:
            print(e)
            return "error"

    def merge_to_workfile(self, destination="DATA/list_channel.csv", **kwargs):
        """
        Process videos in video_list,
        :param kwargs: You can change the search_key by setting file_dir={other search key}. It will visit corresponding
        folders in YouTube_RAW/video_list/{search_key}. If this new search key is not specified,
        the key used to retrieve search results will be used.
        :return: this function will generates video_list.csv in YouTube_RAW folder
        """
        dirpath = self.list_channel

        json_list = [file for file in os.listdir(dirpath) if file.endswith(".json")]
        channel_list = []
        for jsonFile in json_list:
            with open(dirpath + "/" + jsonFile, 'r') as fp:
                lines = fp.readlines()
            for line in lines:
                channel_json = json.loads(line)
                dataObj = {
                    "channelId": channel_json["snippet"]["channelId"],
                    "publishedAt": channel_json["snippet"]["publishedAt"].split("T")[0],
                    "channelName": channel_json["snippet"]["channelTitle"],
                    "homePage": f"https://www.youtube.com/channel/{channel_json['snippet']['channelId']}",
                    "searchKey": jsonFile.replace(".json", ""),
                    "description": channel_json["snippet"]["description"],
                }
                channel_list.append(dataObj)

            df = pd.DataFrame(data=channel_list)
            df = df.groupby('channelId').agg({
                'publishedAt': 'first',
                'channelName': 'first',
                "homePage": 'first',
                "searchKey": lambda x: json.dumps(list(x)),
                "description": 'first',
            })
            df = df.reset_index()
            df.to_csv(destination, index=False)
