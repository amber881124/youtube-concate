from youtube_concate.pipeline.steps.step import Step


# 進pipeline後
class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
