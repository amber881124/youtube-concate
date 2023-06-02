from pprint import pprint

from .step import Step
from .step import StepException


class Search(Step):
    def process(self, data, inputs, utils):
        # 此時的data是:一堆yt物件(有幾個影片id就有幾個yt物件)
        found = []
        for yt in data:
            # yt.captions 是一個字典。裡面裝著某影片的所有字幕
            captions = yt.captions
            try:
                for caption in captions:
                    if inputs['search_term'] in caption:
                        # yt.captions[caption]] 是拿'時間'
                        time = captions[caption]
                        # append整個yt物件，而非只拿yt物件的id，以免之後要用到其他的
                        found.append((yt, caption, time))
            except TypeError as e:
                # 此影片無自動產生字幕
                print(e)
                continue
        pprint(found)
