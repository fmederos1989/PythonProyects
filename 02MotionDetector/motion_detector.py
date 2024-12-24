import cv2, time

first_frame = None

video = cv2.VideoCapture(0)

while True:
    chek, frame = video.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_frame
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    # (cnts,_) = cv2.findContours(thresh_frame)

    cv2.imshow("Capturando", gray_frame)
    cv2.imshow("delta_frame", delta_frame)
    cv2.imshow("thresh_delta", thresh_frame)

    key = cv2.waitKey(1)
    print(gray_frame)
    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()