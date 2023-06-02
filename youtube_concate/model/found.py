# 把每個有相關字的句子當一個物件
class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt
        self.caption = caption
        self.time = time

    def __str__(self):
        return f'<Found(yt = {self.yt})>'

    def __repr__(self):
        context = ' : '.join([
            f'yt = {self.yt}',
            f'caption = {self.caption}',
            f'time = {self.time}'
        ])
        return f'<Found({context})>'


