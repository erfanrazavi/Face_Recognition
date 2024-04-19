import sys

from video import Video
from detector import Detector

def main(*args):
    video_address = args[1] if len(args) > 1 else 0
    detector = Detector('files/face.xml')
    
    for frame in Video(video_address):
        frame.draw_rectangle(detector.get_coordinates(frame.gray_scale()))
        frame.show_frame()



if __name__ == "__main__":
    main(*sys.argv)