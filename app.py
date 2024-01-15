import cv2
from src.data_source import initialize_video, initialize_webcam
from src.helper import detect_license_plate
from src.helper import save_plate



def main():
    harcascade = "./model/haarcascade_russian_plate_number.xml"
    video_path = "./assets/1.mp4"
    cap = initialize_video(video_path)
    plate_cascade = cv2.CascadeClassifier(harcascade)
    min_area = 500
    count = 0

    # ratio ( 16:9)
    target_aspect_ratio = 16 / 9

    while True:
        _, img = cap.read()

        # Detect license plates and get img_roi
        img_roi = detect_license_plate(img, plate_cascade, min_area)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            save_plate(img, img_roi, count)
            count += 1

        # Resize the frame to maintain the desired aspect ratio
        current_height, current_width, _ = img.shape
        current_aspect_ratio = current_width / current_height

        if current_aspect_ratio > target_aspect_ratio:
            new_width = int(target_aspect_ratio * current_height)
            img = cv2.resize(img, (new_width, current_height))
        else:
            new_height = int(current_width / target_aspect_ratio)
            img = cv2.resize(img, (current_width, new_height))

        cv2.imshow("Video", img)


        # to break the loop press q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
