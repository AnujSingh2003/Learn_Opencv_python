"""import cv2
cap=cv2.VideoCapture("D:\Chat Application\ting.mp4")
print("cap",cap)
while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(700,450))
    gray=cv.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray",gray)
    k=cv2.waitKey(25)#lesser the waitkey the video will get slow and viceversa
    if k==ord("q") & 0xff:
        break
    cap.release()
    cv2.destroyAllWindows()"""
    
import cv2
cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("E:\\output.avi",fourcc,20.0,(640,480),0)

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    print("Video opened successfully.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cv2.imshow("frame", frame)
        cv2.imshow("gray", gray)
        output.write(frame)
        k = cv2.waitKey(25)  # lesser the waitkey, the video will get slow and vice versa
        if k == ord("q") & 0xff:
            break

cap.release()
output.release()
cv2.destroyAllWindows()
