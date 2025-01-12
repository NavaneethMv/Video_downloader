from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from nanoid import generate

'''
    This module helps to trim video and music file and saves in appropriate formats.
'''

class Trimmer():
    '''
        Takes filename along with startime ,end time and extension to be saved with,
        returns status code along with saved filename which will be unique.
    '''
    def __init__(self, file_name: str) -> None:
        self.file_name = f"static/{file_name}"
    
    def trim_video(self, start: int, end: int) -> str:
        extension = self.find_ext()
        video_filename = f"{str(generate(size=10))}.{extension}"
        ffmpeg_extract_subclip(self.file_name, start, end, outputfile=f"static/{video_filename}")
        return video_filename
    
    def find_ext(self):
        ext = self.file_name.split('.')
        return ext[1]