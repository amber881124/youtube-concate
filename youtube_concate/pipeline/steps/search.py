from .step import Step
from .step import StepException


class Search(Step):
    def process(self, data, inputs, utils):
        for caption_file in data: # 字典第一層的每個key就是字幕檔名
            captions = data[caption_file] # 整個字典(data)的key(字幕檔名)可取得每個字幕檔的字幕
            for caption in captions:
                if inputs['search_term'] in caption:
                    print('found')
                    print(caption)
