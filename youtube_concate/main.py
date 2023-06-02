from youtube_concate.pipeline.pipeline import Pipeline
from youtube_concate.utils import Utils
from youtube_concate.pipeline.steps.preflight import Preflight
from youtube_concate.pipeline.steps.get_video_list import GetVideoList
from youtube_concate.pipeline.steps.initialize_yt import InitializeYT
from youtube_concate.pipeline.steps.download_captions import DownloadCaptions
from youtube_concate.pipeline.steps.read_caption import ReadCaption
from youtube_concate.pipeline.steps.search import Search
from youtube_concate.pipeline.steps.download_videos import DownloadVideos
from youtube_concate.pipeline.steps.postflight import Postflight


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_term': 'incredible',
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        # DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        Postflight(),
    ]
    utils = Utils()
    # pipeline design pattern
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()

