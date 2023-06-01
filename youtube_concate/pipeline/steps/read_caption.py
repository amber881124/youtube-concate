import os
from pprint import pprint

from .step import Step
from .step import StepException
from youtube_concate.settings import CAPTIONS_DIR


# {'text': 'the brand new', 'start': 19.199, 'duration': 11.92}
class ReadCaption(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            if not utils.caption_file_exists(yt):
                print(f'影片id : {yt.id} 的字幕檔不存在')
                continue
            with open(yt.get_caption_filepath(), 'r') as f:
                captions = {}
                for line in f:
                    caption, start, duration = line.split(', ')
                    caption = caption.split(': ')[-1]
                    caption = caption.replace("'", "").replace('"', '').strip()
                    # print(caption)
                    time = [start.strip().split(': ')[-1], duration.strip().split(': ')[-1].replace("}", "").strip()]
                    # print(time)
                    # 字典(captions):key是caption，value是time
                    # key是caption:因為之後要找關鍵字可以直接用for loop取得caption
                    captions[caption] = time
                # 把此影片的字幕(字典)裝到yt物件的captions屬性
                # 解決雙層字典問題
                yt.captions = captions
        # pprint(data)
        return data




