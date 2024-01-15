import cv2

def initialize_video(video_path):
    cap = cv2.VideoCapture(video_path)
    cap.set(3, 640)
    cap.set(4, 480)
    return cap


def initialize_webcam():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    return cap
