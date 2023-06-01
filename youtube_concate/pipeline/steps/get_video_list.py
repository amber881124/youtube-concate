import scrapetube

from youtube_concate.pipeline.steps.step import Step
from youtube_concate.pipeline.steps.step import StepException


class GetVideoList(Step):
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']
        if utils.video_list_file_exist(channel_id):
            print('Found existing video list file for channel id', channel_id)
            return self.read_file(utils.get_video_list_filepath(channel_id))
        videos = scrapetube.get_channel(channel_id)
        video_id = []
        for video in videos:
            # print("https://www.youtube.com/watch?v="+str(video['videoId']))
            video_id.append(video['videoId'])
        # 把影片id放到檔案裡
        self.write_to_file(video_id, utils.get_video_list_filepath(channel_id))
        return video_id

    @staticmethod
    def write_to_file(video_id, filepath):
        with open(filepath, 'w') as f:
            for id_ in video_id:
                f.write(id_ + '\n')

    @staticmethod
    def read_file(filepath):
        video_id = []
        with open(filepath, 'r') as f:
            for id_ in f:
                video_id.append(id_.strip())
        return video_id
