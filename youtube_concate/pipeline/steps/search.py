from .step import Step
from .step import StepException


class Search(Step):
    def process(self, data, inputs, utils):
        # 此時的data是:一堆yt物件(有幾個影片id就有幾個yt物件)
        for yt in data:
            print(f'現在影片id是:{yt.id}')
            try:
                for caption in yt.captions:
                    if inputs['search_term'] in caption:
                        print('found')
                        print(caption)
            except TypeError as e:
                # 此影片無自動產生字幕
                print(e)
                continue
