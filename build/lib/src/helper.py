import cv2

# for detection of number plate
def detect_license_plate(img, plate_cascade, min_area):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h
        if area > min_area:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(img, "License Plate", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
            img_roi = img[y:y + h, x:x + w]
            cv2.imshow("ROI", img_roi)

    cv2.imshow("Result", img)



# for saving the plate number
    
def save_plate(img, img_roi, count):
    cv2.imwrite("plate_" + str(count) + ".jpg", img_roi)
    cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
    cv2.imshow("Results", img)
    cv2.waitKey(500)
