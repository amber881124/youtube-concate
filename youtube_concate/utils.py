import os

from youtube_concate.settings import CAPTIONS_DIR
from youtube_concate.settings import DOWNLOADS_DIR
from youtube_concate.settings import VIDEOS_DIR


# 放helper function
class Utils:
    def __init__(self):
        pass

    @staticmethod
    def create_dirs():
        os.makedirs(DOWNLOADS_DIR, exist_ok=True)
        os.makedirs(CAPTIONS_DIR, exist_ok=True)
        os.makedirs(VIDEOS_DIR, exist_ok=True)

    @staticmethod
    def get_video_list_filepath(channel_id):
        return os.path.join(DOWNLOADS_DIR, channel_id + '.txt')

    def video_list_file_exist(self, channel_id):
        path = self.get_video_list_filepath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def get_caption_filepath(video_id):
        caption_path = os.path.join(CAPTIONS_DIR, video_id + '.txt')
        return caption_path

    def caption_file_exists(self, video_id):
        path = self.get_caption_filepath(video_id)
        # 檔案是否存在，且不是空檔案
        # 有可能檔案已建立，但內容是空的(例如:執行錯誤)
        return os.path.exists(path) and os.path.getsize(path) > 0


