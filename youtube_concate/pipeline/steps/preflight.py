from youtube_concate.pipeline.steps.step import Step


# 進pipeline前
class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()
        