import sys
from googleapiclient.discovery import build
import json
from configparser import ConfigParser
import os
from httplib2 import ServerNotFoundError
import re

CONFIG = "config.ini"
config = ConfigParser(allow_no_value=True)
config.read(CONFIG)


class _CrawlerObject():
    """Base class to configure file saving paths"""

    def __init__(self):

        # more permanent
        self.DEVELOPER_KEY = None
        self.YOUTUBE_API_SERVICE_NAME = None
        self.YOUTUBE_API_VERSION = None
        self.KEYS_PATH = None

        # more changing
        self.youtube = None
        self.code_index = -1
        self._build()

    def _build(self):
        self._fetch_vars()
        try:
            os.mkdir("DATA")
        except OSError:
            print("Directory already exists %s" % "DATA")
        else:
            print("Successfully created the directory %s " % "DATA")

        # api
        try:
            self._try_next_id()
            self.youtube = build(
                self.YOUTUBE_API_SERVICE_NAME,
                self.YOUTUBE_API_VERSION,
                developerKey=self.DEVELOPER_KEY,
                cache_discovery=False)
            print("BUILD SUCCESS")
        except ServerNotFoundError:
            print("BUILD FAILED - NO INTERNET CONNECTION")
            sys.exit(0)

    def _fetch_vars(self):
        config.read(CONFIG)
        self.YOUTUBE_API_SERVICE_NAME = config.get("api", "youtube_api_service_name")
        self.YOUTUBE_API_VERSION = config.get("api", "youtube_api_version")
        self.KEYS_PATH = config.get("api", "keys_path")
        with open(self.KEYS_PATH, 'r+') as fp:
            self.codes = fp.readlines()

        # datapath
        self.list_video = config.get("datapath", "list_video")
        self.list_channel = config.get("datapath", "list_channel")
        self.data_video_json = config.get("datapath", "data_video_json")
        self.data_video_stream = config.get("datapath", "data_video_stream")
        self.data_channel_json = config.get("datapath", "data_channel_json")
        self.data_comment_json = config.get("datapath", "data_comment_json")
        self.data_subtitle_json = config.get("datapath", "data_subtitle_json")
        self.youtube_csv = config.get("datapath", "YouTube_CSV")

    def _try_next_id(self):
        """
        Update the API
        :return:
        """
        if self.code_index + 1 < len(self.codes):
            self.code_index += 1
            self.DEVELOPER_KEY = self.codes[self.code_index].strip()  # Update a new key
            self.youtube = build(
                self.YOUTUBE_API_SERVICE_NAME,
                self.YOUTUBE_API_VERSION,
                developerKey=self.DEVELOPER_KEY,
                cache_discovery=False)
            print(f"Update Developer Key:{self.DEVELOPER_KEY}")
        else:
            print("running out keys")
            sys.exit(0)
        self.DEVELOPER_KEY = self.codes[self.code_index].strip()  # Use your own Keys.

    def _get_error_code(self, message):
        error = json.loads(message)
        if error["error"]["errors"][0]["reason"]:
            reason = error["error"]["errors"][0]["reason"]
            if reason == "dailyLimitExceeded" or reason == "quotaExceeded":
                print("Running out of quotas. Updating API key.")
                return "update_API_key"
            elif reason == 'badRequest':
                print("API deprecated. Delete API from key file.")
                return "update_API_key"
            elif reason == 'forbidden':
                print(error["error"]["errors"][0]["message"])
                return 'forbidden'

    def _toDayFormat(self, date):
        return f"{date.year}-{date.month}-{date.day}"

    def _isCrawled(self, file_name):
        return os.path.exists(file_name)

    def _write_item(self, file_path, items):
        with open(file_path, 'a+') as fp:
            for item in items:
                fp.write(json.dumps(item) + "\n")

    def _get_search_short(self, text):
        aphanum = re.sub(r'[^a-zA-Z\s]', '~', text)
        return ''.join(aphanum)
