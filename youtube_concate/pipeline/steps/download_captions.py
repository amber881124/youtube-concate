from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api import TranscriptsDisabled
from youtube_transcript_api import NoTranscriptFound

from youtube_concate.pipeline.steps.step import Step
from youtube_concate.pipeline.steps.step import StepException


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        for yt in data:
            print(f'Downloading caption for {yt.id}')
            if utils.caption_file_exists(yt):
                print('found existing caption file')
            try:
                srt = YouTubeTranscriptApi.get_transcript(yt.id, languages=['en'])
            except (TranscriptsDisabled, NoTranscriptFound) as e:
                print(f'{repr(e).split("(")}[0] when downloading caption for{yt.id}')
                continue
            with open(yt.caption_filepath, "w", encoding='utf-8') as f:
                # iterating through each element of list srt
                for i in srt:
                    # writing each element of srt on a new line
                    f.write(f'{format(i)}\n')
        return data

