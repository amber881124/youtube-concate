import scrapetube

from youtube_concate.pipeline.steps.step import Step
from youtube_concate.pipeline.steps.step import StepException


class GetVideoList(Step):
    def process(self, data, inputs):
        channel_id = inputs['channel_id']
        videos = scrapetube.get_channel(channel_id)
        video_links = []
        for video in videos:
            # print("https://www.youtube.com/watch?v="+str(video['videoId']))
            video_links.append("https://www.youtube.com/watch?v=" + str(video['videoId']))
        return video_links

