import cv2
import sys

catCascade = cv2.CascadeClassifier('cascade.xml')

video_capture = cv2.VideoCapture(0)


def interperetCode():
    frame = cv2.imread("frame.png")
    gray = gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cats = catCascade.detectMultiScale(
        frame,
        scaleFactor=1.15,
        minNeighbors=3,
    )
    x, y, w, h = cats[0]
    c1 = [(2 * x + w)/2, (2 * y + h)/2]

    x, y, w, h = cats[1]
    c2 = [(2 * x + w)/2, (2 * y + h)/2]

    x_diff = c1[0] - c2[0]
    y_diff = c1[1] - c2[1]

    row1 = [x_diff * 0.25, x_diff * 0.5, x_diff * 0.75, x_diff]
    row2 = [0, x_diff * 0.25, x_diff * 0.5, x_diff * 0.75]

    bin_str = ""
    for i in row1:
        x_val = c1[0] + i
        if np.any(gray[x_val, c1[1]] < 20):
            bin_str += "1"
        else:
            bin_str += "0"

    for i in row2:
        x_val = c2[0] + i
        if np.any(gray[x_val, c2[1]] < 20):
            bin_str += "1"
        else:
            bin_str += "0"

    return bin_str



while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cats = catCascade.detectMultiScale(
        frame,
        scaleFactor=1.15,
        minNeighbors=3,
    )

    for (x, y, w, h) in cats:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    if len(cats) >= 2:
        frame.imwrite("frame.png")
        code = int(interperetCode(), 2)
        cv2.destroyAllWindows()

    cv2.imshow('Video', frame)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(code)
video_capture.release()
cv2.destroyAllWindows()

