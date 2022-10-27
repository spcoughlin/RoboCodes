def big_main():
    import cv2
    import sys

    faceCascade = cv2.CascadeClassifier('cascade.xml')

    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGR565)

        faces = faceCascade.detectMultiScale(
            frame,
            scaleFactor=1.15,
            minNeighbors=3,
        )

        for (x, y, w, h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    big_main()
