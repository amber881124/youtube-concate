from moviepy.editor import VideoFileClip
from moviepy.editor import concatenate_videoclips
from .step import Step


class EditVideo(Step):
    def process(self, data, inputs, utils):
        search_term = inputs['search_term']
        channel_id = inputs['channel_id']
        clips = []

        for found in data:
            start, end = self.parse_caption_time(found.time)
            filepath = found.yt.video_filepath
            video = VideoFileClip(filepath).subclip(start, end)
            clips.append(video)
            if len(clips) >= inputs['limit']:
                break

        final_clip = concatenate_videoclips(clips)
        output_filepath = utils.get_output_filepath(channel_id, search_term)
        final_clip.write_videofile(output_filepath, fps=25)

    @staticmethod
    def parse_caption_time(caption_time):
        start = caption_time[0]
        end = caption_time[1]
        return start, end
