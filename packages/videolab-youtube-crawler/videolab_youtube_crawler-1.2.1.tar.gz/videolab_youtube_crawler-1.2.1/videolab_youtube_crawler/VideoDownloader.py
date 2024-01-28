import asyncio
import os
from concurrent.futures import ProcessPoolExecutor
import re

import pandas as pd
from yt_dlp import YoutubeDL

from videolab_youtube_crawler.CrawlerObject import _CrawlerObject

# choco install ffmpeg

"""Download MP4 file from YouTube"""


class VideoDownloader(_CrawlerObject):

    def __init__(self):
        self.failed_videos_due_to_unavailability = []
        self.failed_without_reason = []
        self.PPE = ProcessPoolExecutor()
        super().__init__()

    def download_videos_in_list(self, video_list_workfile=f"DATA/list_video.csv", audio=False, **kwargs):
        """
        Download MP4 file from the list_video workfile
        :param audio:
        :param video_list_workfile: File to process
        :param kwargs:
        :return:
        """
        qual = kwargs.get('quality', 'worst')
        if qual == 'worst':
            self.quality = 'wv+wa'
        else:
            self.quality = 'bv+ba'
        core = kwargs.get("core", 5)
        batch = kwargs.get("batch", 10)
        video_column = kwargs.get('video_id', 'videoId')
        self.video_data_dir = kwargs.get('video_data_dir', self.data_video_stream)
        df = pd.read_csv(video_list_workfile)
        video_list = list(df[video_column])
        asyncio.run(self._download_video_list(video_list, self.video_data_dir, audio, core, batch))

    def clean_files(self, video=True, audio=True, **kwargs):
        """
        Clean the data folder to save spaces.
        :param video:
        :param audio:
        :param kwargs:
        :return:
        """
        self.video_data_dir = kwargs.get('video_data_dir', self.data_video_stream)
        for dirpath, dirnames, filenames in os.walk(self.video_data_dir):
            for filename in filenames:
                fpath = os.path.join(dirpath, filename)
                try:
                    if video and '.mp4' in filename:
                        if not bool(re.search(r"[0-9A-Za-z_-]{11}.mp4", filename)):
                            os.remove(fpath)
                            print('remove:', fpath)
                    if audio and '.mp3' in filename:
                        if not bool(re.search(r"[0-9A-Za-z_-]{11}.mp3", filename)):
                            os.remove(fpath)
                            print('remove:', fpath)
                except FileNotFoundError:
                    print("Cleaning error: File not found!")
                except PermissionError:
                    print("Cleaning error: Permission denied!")
                except Exception as e:
                    print(f"A cleaning error occurred: {e}")

    async def _download_video_list(self, video_list, video_data_dir, audio, core, batch=10):
        vids = [[]]
        for video_id in video_list:
            vid = video_id[1:]
            dir1 = f"{video_data_dir}/{vid}/{vid}.mp4"
            dir2 = f"{video_data_dir}/{vid}/{vid}.mp4.mkv"
            if not self._isCrawled(dir1) and not self._isCrawled(dir2):  # check if video existed
                print(f"Crawling a video mp4 for {vid}....")
                try:
                    os.mkdir(f"{video_data_dir}/{vid}")
                    pass
                except OSError:
                    pass
                if len(vids[-1]) == batch:  # crawl batch videos every time
                    vids.append([])
                vids[-1].append(vid)  # add the video to the last list in vids
            else:
                print(f"Skip {vid}, video stream already crawled")
            if len(vids) == core and len(vids[-1]) == batch:  # if the vids have core lists and the last batch is full
                await self._download_list_async(vids, video_data_dir, audio)
                vids = [[]]
        for b in vids:  # process the remaining videos
            if len(b) > 0:
                await self._download_list_async([b], video_data_dir, audio)

    async def _download_list_async(self, sublist, video_data_dir, audio):
        URLs = [[f'https://www.youtube.com/watch?v={video_id}' for video_id in batch] for batch in sublist]
        ydl_opts = {
            'format': self.quality,
            'progress_hooks': [my_hook],
            'throttled-rate': '2000K',
            'outtmpl': f'{video_data_dir}/%(id)s/%(id)s.mp4'
        }
        if audio:
            ydl_opts['keepvideo'] = True
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        try:
            loop = asyncio.get_event_loop()
            futs = [loop.run_in_executor(None, YoutubeDL(ydl_opts).download, url) for url in URLs]
            await asyncio.gather(*futs)
        except:
            print('Video collect failed', URLs)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now post-processing ...')
