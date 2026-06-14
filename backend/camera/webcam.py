import cv2

class Webcam:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

    def read_frame(self):
        success, frame = self.cap.read()

        if not success:
            return None

        return frame

    def release(self):
        self.cap.release()