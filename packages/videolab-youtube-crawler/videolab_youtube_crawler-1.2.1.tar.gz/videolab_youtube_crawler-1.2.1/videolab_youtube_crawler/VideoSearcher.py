import os
import re
from videolab_youtube_crawler.CrawlerObject import _CrawlerObject
from datetime import datetime, timedelta, date
import pytz
from googleapiclient.errors import HttpError
import sys
import pandas as pd
import json


class VideoSearcher(_CrawlerObject):
    """Perform search of keywords and get the list of videos"""

    def __init__(self):
        super().__init__()

    def search(self, search_key, start_day, start_month, start_year, end_day, end_month, end_year, day_span, **kwargs):
        """
        Crawl the video between two given days
        :param search_key:
        :param start_day:
        :param start_month:
        :param start_year:
        :param end_day:
        :param end_month:
        :param end_year:
        :param day_span:
        :return:
        """
        self.search_key = search_key
        self.region_code = kwargs.get("region_code", "US")
        # counter number of days of videos to crawl
        start = date(start_year, start_month, start_day)  # start date of crawling
        end = date(end_year, end_month, end_day)  # end date of crawling
        assert start < end
        assert type(day_span) == int and day_span >= 1
        delta_time = end - start
        day_count = int(delta_time.days)

        start_datetime = datetime(year=start_year, month=start_month, day=start_day, tzinfo=pytz.utc)
        date_mark = self._toDayFormat(start_datetime)
        delta = timedelta(hours=24 * day_span)

        try:
            os.mkdir(f"{self.list_video}/")
        except OSError:
            print("Directory already exists %s" % self.list_video)

        count = 0
        while count <= day_count:
            print(f"start crawling:{date_mark}")
            # Initialize the paths
            video_file_name = f"{self._get_search_short(self.search_key)}_{date_mark}.json"
            self.data_file_path = f"{self.list_video}{video_file_name}"
            # crawl data, update start date.
            if not self._isCrawled(self.data_file_path):
                self._crawl_data_n_day(start_datetime, delta)
            else:
                print(f"Skip {self.data_file_path}. Date already crawled. ")
            start_datetime += delta
            date_mark = self._toDayFormat(start_datetime)
            count += day_span

    def _crawl_data_n_day(self, start_datetime, delta):
        """
        Add one day to the next crawl
        :param start_datetime:
        :return:
        """
        print(f"crawling video list....", str(delta))
        self._crawl_data(start_datetime, start_datetime + delta)

    def _crawl_data(self, start_time, end_time):
        """
        Iterate through all nextPageToken to get all available videos
        :param start_time: The beginning datetime
        :param end_time: The cutoff datetime
        :return:
        """
        response = self._search_data(self.data_file_path, start_time, end_time)
        total_result = response["pageInfo"]["totalResults"]
        if "nextPageToken" not in response:
            start_time_mark = self._toDayFormat(start_time)
            end_time_mark = self._toDayFormat(end_time)
            print(f"total results:{str(total_result)} between {start_time_mark} and {end_time_mark}")
            return
        while True:
            response = self._search_data(self.data_file_path, start_time, end_time, response["nextPageToken"])
            if "nextPageToken" not in response:
                start_time_mark = self._toDayFormat(start_time)
                end_time_mark = self._toDayFormat(end_time)
                print(f"total results:{str(total_result)} between {start_time_mark} and {end_time_mark}")
                break

    def _search_data(self, file_path, start_time, end_time, page_token=None):
        """
        Crawl a list of videos which matches {search_key}. Save the data in {video_list_dir}
        JSON returned from https://developers.google.com/youtube/v3/docs/search/list
        :param file_path: file path to save the collected video
        :param start_time: collect video from this date
        :param end_time: collect video to this date
        :param page_token: Do not modify this param
        :return:
        """
        part = "snippet"
        try:
            if page_token:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      q=self.search_key,
                                                      pageToken=page_token,
                                                      type="video",
                                                      publishedAfter=start_time.isoformat(),
                                                      publishedBefore=end_time.isoformat(),
                                                      regionCode=self.region_code
                                                      ).execute()
            else:
                response = self.youtube.search().list(part=part,
                                                      maxResults=50,
                                                      q=self.search_key,
                                                      type="video",
                                                      publishedAfter=start_time.isoformat(),
                                                      publishedBefore=end_time.isoformat(),
                                                      regionCode=self.region_code
                                                      ).execute()
            self._write_item(file_path, response["items"])  # remove duplicate
            return response
        except HttpError as e:
            error = self._get_error_code(e.content)
            if error == "update_API_key":
                self._try_next_id()
                return self._search_data(file_path, start_time, end_time, page_token)
        except Exception as e:
            print(e)
            sys.exit(0)

    def merge_to_workfile(self, destination="DATA/list_video.csv"):
        """
        This function merges videos on different days to a csv worklist. Later the crawler will use the worklist to collect
        all video data.
        Search results will be merged into video_to_collect.csv Unique identifiers: video id and search key
        :param destination: save to a csv work file containing all videos to be collected.
        You can change the video_search_list to other folders by setting file_dir={other search key}
        :return: this function will generates video_list.csv in YouTube_RAW folder
        """

        dirpath = self.list_video
        video_list = []
        json_list = (file for file in os.listdir(dirpath) if file.endswith(".json"))
        # Save video meta data of all the videos saved in {video_list_path}
        for filename in json_list:
            with open(dirpath + filename, 'r') as fp:
                line = fp.readline()
                while line and line != "":
                    try:
                        search_result = json.loads(line)
                        if "videoId" in search_result["id"]:
                            video_list.append({
                                "videoId": ":" + search_result["id"]["videoId"],
                                "url": f'https://www.youtube.com/watch?v={search_result["id"]["videoId"]}',
                                "channelId": search_result["snippet"]["channelId"],
                                "publishedAt": search_result["snippet"]["publishedAt"].split("T")[0],
                                "searchKey": re.sub(r'_\d{4}-\d{1,2}-\d{1,2}.json$', '', filename),
                                "dateAdded": datetime.now()
                            })
                    except json.JSONDecodeError:
                        print("JSON error", line)
                    finally:
                        line = fp.readline()

        df = pd.DataFrame(data=video_list)
        if os.path.exists(destination):
            tdf = pd.read_csv(destination)
            df = pd.concat([tdf, df])
            df = df.drop_duplicates(subset=["videoId"], keep='last')
            df.to_csv(destination, index=False)
            print(f"new videos added to work file {destination}")
        else:
            df.to_csv(destination, index=False)
            print(f"new work file created at {destination}")
