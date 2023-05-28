import time
import scrapetube


CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'

start = time.time()
videos = scrapetube.get_channel(CHANNEL_ID)
video_links = []
for video in videos:
    # print("https://www.youtube.com/watch?v="+str(video['videoId']))
    video_links.append("https://www.youtube.com/watch?v=" + str(video['videoId']))
print(video_links)
print(len(video_links))
end = time.time()
print(f'總共費時 : {end - start} 秒')
