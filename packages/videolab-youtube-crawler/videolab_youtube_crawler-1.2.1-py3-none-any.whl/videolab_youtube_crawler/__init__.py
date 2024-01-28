from configparser import ConfigParser
from datetime import date
import os

# You can configure here or in the generated config.ini file
# If you configure directly in this code, make sure to delete existing config.ini to reflect the changes
__all__ = ['CrawlerObject', 'VideoSearcher']
__version__ = '1.2.1'

CONFIG = "config.ini"


def init_config():
    if os.path.exists(CONFIG):
        print("Configuration file config.ini existed! Delete the file before resetting!")
        return

    datapath = {
        "list_video": f"DATA/list_video/",
        "list_channel": f"DATA/list_channel/",
        "data_video_json": "DATA/data_video_json/",
        "data_channel_json": "DATA/data_channel_json/",
        "data_subtitle_json": "DATA/data_subtitle_json/",
        "data_comment_json": "DATA/data_comment_json/",
        "data_video_stream": "DATA/data_video_stream",
        "YouTube_CSV": "DATA/YouTube_CSV/"
    }

    api = {
        "KEYS_PATH": "DEVELOPER_KEY.txt",
        "YOUTUBE_API_SERVICE_NAME": "youtube",
        "YOUTUBE_API_VERSION": "v3",
        "YOUTUBE_URL": "https://www.googleapis.com/youtube/v3/"
    }

    config = ConfigParser(allow_no_value=True)
    config.read(CONFIG)

    config.add_section('datapath')
    config.set('datapath', '; all sub directories in this section will be under RAW_PARENT_PATH')
    for k, v in datapath.items():
        config.set("datapath", k, v)

    config.add_section('api')
    for k, v in api.items():
        config.set("api", k, v)

    with open(CONFIG, 'w') as f:
        config.write(f)


from videolab_youtube_crawler.VideoSearcher import VideoSearcher
from videolab_youtube_crawler.VideoCrawler import VideoCrawler
from videolab_youtube_crawler.VideoDownloader import VideoDownloader
from videolab_youtube_crawler.ChannelCrawler import ChannelCrawler
from videolab_youtube_crawler.CommentCrawler import CommentCrawler
from videolab_youtube_crawler.SubtitleCrawler import SubtitleCrawler
from videolab_youtube_crawler.ChannelSearcher import ChannelSearcher
