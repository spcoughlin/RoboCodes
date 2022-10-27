import cv2
import sys
import numpy as np

catCascade = cv2.CascadeClassifier('cascade.xml')

video_capture = cv2.VideoCapture(0)

global cats
cats = None

def interperetCode(c1, c2, gray):
    x_diff = abs(c2[0] - c1[0])

    row1 = [x_diff * 0.25, x_diff * 0.5, x_diff * 0.75, x_diff]
    row2 = [0, x_diff * 0.25, x_diff * 0.5, x_diff * 0.75]

    bin_str = ""
    for i in row1:
        x_val = c1[0] + int(i)
        y = c1[1]
        print(x_val, y)
        if np.any(gray[y, x_val] < 50):
            bin_str += "1"
        else:
            bin_str += "0"
        x_val = 0
        y = 0

    for i in row2:
        x_val = c1[0] + int(i)
        y = c2[1]
        print(x_val, y)
        if np.any(gray[y, x_val] < 50):
            bin_str += "1"
        else:
            bin_str += "0"
        x_val = 0
        y = 0

    print(bin_str)
    cv2.imwrite("graywdots.png", gray)
    return bin_str



while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cats = catCascade.detectMultiScale(
        gray,
        scaleFactor=1.15,
        minNeighbors=5,
    )

    for (x, y, w, h) in cats:
        cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)

    if len(cats) >= 2:
        x, y, w, h = cats[0]
        c1 = [int((2 * x + w)/2), int((2 * y + h)/2)]

        x, y, w, h = cats[1]
        c2 = [int((2 * x + w)/2), int((2 * y + h)/2)]

        if c1[0] < c2[0]: # makiing sure c1 is the one on the left
            pass
        elif c1[0] > c2[0]:
            temp = c1
            c1 = c2
            c2 = temp

        code = int(interperetCode(c1, c2, gray), 2)
        break

    cv2.imshow('Video', frame)

    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(code)
video_capture.release()
cv2.destroyAllWindows()

