import cv2

catCascade = cv2.CascadeClassifier('cascade.xml')
video_capture = cv2.VideoCapture(0)
print("Awaiting Code...")

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cats = catCascade.detectMultiScale(
        gray,
        scaleFactor=1.015, # should be 1.01
        minNeighbors=5, # should be 4
    )

    for (x, y, w, h) in cats:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()