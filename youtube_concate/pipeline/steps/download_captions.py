import time
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound

from youtube_concate.pipeline.steps.step import Step
from youtube_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        for video_id in data:
            print(f'Downloading caption for {video_id}')
            if utils.caption_file_exists(video_id):
                print('found existing caption file')
            try:
                srt = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            except (TranscriptsDisabled, NoTranscriptFound) as e:
                print(f'{repr(e).split("(")}[0] when downloading caption for{video_id}')
                continue
            with open(utils.get_caption_filepath(video_id), "w", encoding='utf-8') as f:
                # iterating through each element of list srt
                for i in srt:
                    # writing each element of srt on a new line
                    f.write(f'{format(i)}\n')
        end = time.time()
        print(f'took {end - start} seconds')

