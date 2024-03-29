import os

from youtube_concate.settings import CAPTIONS_DIR
from youtube_concate.settings import VIDEOS_DIR


# 把youtube資料結構成class (字典 -> class)
# 此class放:每個影片(物件)的各個屬性
class YT:
    def __init__(self, video_id):
        self.id = video_id
        self.url = self.video_url()
        self.video_filepath = self.get_video_filepath()
        self.caption_filepath = self.get_caption_filepath()
        self.captions = None

    def video_url(self):
        url = f'https://www.youtube.com/watch?v={self.id}'
        return url

    def get_video_filepath(self):
        video_path = os.path.join(VIDEOS_DIR, self.id + '.mp4')
        return video_path

    def get_caption_filepath(self):
        caption_path = os.path.join(CAPTIONS_DIR, self.id + '.txt')
        return caption_path

    def __str__(self):
        return f'<YT(id = {self.id})>'

    def __repr__(self):
        context = ' : '.join([
            f'id = {self.id}',
            f'video_filepath = {self.video_filepath}',
            f'caption_filepath = {self.caption_filepath}'
        ])
        return f'<YT({context})>'



