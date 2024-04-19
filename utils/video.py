import cv2


class Frame:
    RECTANGLR_COLOR = (0 , 255 , 0)
    RECTANGLR_WIDTH = 10
    WINDOW_TITLE = 'my video'
    
    def __init__(self , frame) -> None:
        self.__frame = frame
        
    def gray_scale(self):
        return cv2.cvtColor(self.__frame , cv2.COLOR_BGR2GRAY)

    def draw_rectangle(self , coordinates):
        for x , y , w , h in coordinates:
            cv2.rectangle(self.__frame, (x ,y) , (x+w , y+h) , Frame.RECTANGLR_COLOR , Frame.RECTANGLR_WIDTH)
            
    def show_frame(self):
        cv2.imshow(Frame.WINDOW_TITLE , self.__frame)

class Video:
    def __init__(self , address):
        self.__video = cv2.VideoCapture(address)
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        is_there_a_frame , frame  = self.__video.read()
        key = cv2.waitKey(1)
        print(key , 'pressed')
        if key == 27 or not is_there_a_frame:
            self.__video.release()
            raise StopIteration
        return Frame(frame)
        
    
    
    