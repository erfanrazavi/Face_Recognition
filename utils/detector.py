import cv2

class Detector:
    def __init__(self , address) :
        self.trained_data = cv2.CascadeClassifier(address)        
    
    def get_coordinates(self , gray_scale_image):
        return self.trained_data.detectMultiScale(gray_scale_image)