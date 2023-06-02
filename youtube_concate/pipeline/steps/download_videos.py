from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

from .step import Step
from youtube_concate.settings import VIDEOS_DIR


class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        # print(len(data))  # 361
        yt_set = set([found.yt for found in data])  # 降低重複性，一個影片有多次出現關鍵字，就會有多個found.yt
        print(f'videos to download = {len(yt_set)}')  # 211

        for yt in yt_set:
            if utils.video_file_exists(yt):
                print(f'{yt.id}影片檔已存在')
                continue

            video = YouTube(yt.url)
            try:
                video = video.streams.filter(file_extension='mp4', res='720p').first()
                video.download(output_path=VIDEOS_DIR, filename=f'{yt.id}.mp4')
            except AgeRestrictedError as e:
                print(f'{yt.id} : {e}')
                continue
            except AttributeError as e:
                print(f'{yt.id} : {e}')
                continue
        return data
