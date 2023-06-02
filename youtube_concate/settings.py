from dotenv import load_dotenv
import os

load_dotenv()
YT_API_KEY = os.getenv('YT_API_KEY')

DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
OUTPUTS_DIR = 'outputs'



