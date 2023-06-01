import os
from pprint import pprint

from .step import Step
from .step import StepException
from youtube_concate.settings import CAPTIONS_DIR


# {'text': 'the brand new', 'start': 19.199, 'duration': 11.92}
class ReadCaption(Step):
    def process(self, data, inputs, utils):
        data = {}
        for caption_file in os.listdir(CAPTIONS_DIR):
            with open(os.path.join(CAPTIONS_DIR, caption_file), 'r') as f:
                caption = {}
                for line in f:
                    text, start, duration = line.split(', ')
                    text = text.split(': ')[-1]
                    text = text.replace("'", "").replace('"', '').strip()
                    # print(text)
                    # time = str(start.strip().split(': ')[-1]) + ' ; ' + str(duration.strip().split(': ')[-1].replace("}", "").strip())
                    time = [start.strip().split(': ')[-1], duration.strip().split(': ')[-1].replace("}", "").strip()]
                    # print(time)
                    caption[text] = time
            data[caption_file] = caption
        # pprint(data)
        return data




