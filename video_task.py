import cv2

cap = cv2.VideoCapture("video.mp4")

w,h = 320,240
out = cv2.VideoWriter("output.avi",
                      cv2.VideoWriter_fourcc(*'XVID'),
                      20,(w,h))

while True:
    ret,frame = cap.read()
    if not ret:
        break

    r = cv2.resize(frame,(w,h))
    cv2.imshow("Video",r)
    out.write(r)

    if cv2.waitKey(1)==27:
        break

cap.release()
out.release()
cv2.destroyAllWindows()