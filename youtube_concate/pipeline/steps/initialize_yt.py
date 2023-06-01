from .step import Step
from .step import StepException
from youtube_concate.pipeline.model.yt import YT


class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(video_id) for video_id in data]


