from pprint import pprint

from .step import Step
from youtube_concate.model.found import Found


class Search(Step):
    def process(self, data, inputs, utils):
        found = []
        # 此時的data是:一堆yt物件(有幾個影片id就有幾個yt物件)
        for yt in data:
            # yt.captions 是一個字典。裡面裝著某影片的所有字幕
            captions = yt.captions
            # 如果沒有字幕(None)就跳過
            if not captions:
                continue
            for caption in captions:
                if inputs['search_term'] in caption:
                    # captions[caption]] 是拿'時間'
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    # found(清單)裡面放Found物件
                    found.append(f)

        return found
