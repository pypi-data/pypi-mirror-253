from youtube_transcript_api import YouTubeTranscriptApi
from videolab_youtube_crawler.CrawlerObject import _CrawlerObject
import pandas as pd
from configparser import ConfigParser
import json
import os
import asyncio
import re
# !pip install deepmultilingualpunctuation
from deepmultilingualpunctuation import PunctuationModel

NUMERR_FLAG = -1
STRERR_FLAG = "unknown"

CONFIG = "config.ini"
config = ConfigParser(allow_no_value=True)
config.read(CONFIG)


class SubtitleCrawler(_CrawlerObject):

    def __init__(self):
        super().__init__()
        self.model = PunctuationModel()

    def crawl_subtitles_in_list(self, **kwargs):
        filename = kwargs.get("videos_to_collect", f"DATA/list_video.csv")
        video_id = kwargs.get("video_id", "videoId")
        save_dir = self.data_subtitle_json
        core = kwargs.get("core", 8)

        if not os.path.exists(save_dir):
            os.mkdir(save_dir)

        df = pd.read_csv(filename)
        asyncio.run(self._start_crawling(df, video_id, save_dir, core))

    async def _start_crawling(self, df, video_id, save_dir, core):
        coros = []
        for vid in df[video_id]:
            if not os.path.exists(save_dir + vid[1:] + ".json"):
                print(f"crawling subtitle: {vid[1:]}")
                coros.append(asyncio.gather(self._get_subscription(vid, save_dir)))
                if len(coros) % core == 0:
                    await asyncio.gather(*coros)
                    coros = []

            else:
                print(f'Subtitle {vid} crawled skipped')
        if len(coros) > 0:
            await asyncio.gather(*coros)

    async def _get_subscription(self, vid, save_dir):
        transcript = self._crawl(vid[1:])
        if transcript:
            with open(save_dir + vid[1:] + ".json", 'w+') as fp:
                fp.write(json.dumps(transcript) + "\n")
            print(f'Subtitle {vid} crawled')
        else:
            print(f'Subtitle {vid} crawled failed')

    def _crawl(self, vid):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(vid)
            return transcript
        except:
            return None

    def split_caption_by_sentences(self, **kwargs):
        subtitle_dir = kwargs.get('subtitle_dir', self.data_subtitle_json)

        # List all files in the directory
        file_list = os.listdir(subtitle_dir)
        save_dir=subtitle_dir
        if save_dir.endswith('/'):
            save_dir = save_dir[:-1]
        save_dir=save_dir+'_sentsplit'
        if not os.path.exists(save_dir):
            os.mkdir(save_dir)
            print('Save new subtitle jsons to', save_dir)

        # Iterate through the files
        for filename in file_list:
            if os.path.isfile(os.path.join(subtitle_dir, filename)) and filename.endswith('.json'):
                filedir = f'{subtitle_dir}/{filename}'
                if not os.path.isfile(f'{save_dir}/{filename}'):
                    print('convert', filename)
                    with open(filedir, 'r') as fp:
                        jobj = json.load(fp)
                    try:
                        subtitle = self._convert_to_sentence_timestamps(jobj)
                        with open(f'{save_dir}/{filename}', 'w+') as fp:
                            fp.write(json.dumps(subtitle))
                    except Exception as ex:
                        print('error', ex)
                else:
                    print('skip', filedir)



    def _convert_to_sentence_timestamps(self, subtitles):
        word_ts = []
        for i in range(len(subtitles)):
            tokens = subtitles[i]['text'].strip().split()
            if len(tokens) == 0:
                continue
            if i + 1 < len(subtitles):
                gap = (subtitles[i + 1]['start'] - subtitles[i]['start']) / len(tokens)
            else:
                gap = subtitles[i]['duration'] / len(tokens)
            wts = [(tokens[j], subtitles[i]['start'] + j * gap) for j in range(len(tokens))]
            word_ts += wts
        if len(word_ts) == 0:
            return []
        all_txt = ' '.join([x['text'] for x in subtitles])
        txt_punc = self.model.restore_punctuation(all_txt)
        token_buffer = []
        timestamps = []
        for original, punc in zip(word_ts, txt_punc.split()):
            token_buffer.append([original[0], punc, original[1]])
            if re.match(r'[.?!;]', punc[-1]):
                timestamps.append(token_buffer)
                token_buffer = []
        if len(token_buffer) > 0:
            timestamps.append(token_buffer)
        # merge tokens
        for i in range(len(timestamps)):
            tokens = timestamps[i]
            txt = ' '.join([t[1] for t in tokens])
            timestamp = {
                'text': txt,
                'start': round(tokens[0][2], 2),
                'end': round(tokens[-1][2], 2)
            }
            timestamps[i] = timestamp
        return timestamps
