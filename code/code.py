
# this code in not still perfect 
from cv2 import eye_cascade
import cv2 
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')
def detect_eyes(frame):
    gray=cv2.cvtColor(frame.cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            th,eye=cv2.threshold(roi_color[ey:ey+eh,ex:ex+ew],20,255,cv2.THRESH_BINARY_INV)
            avg_color=cv2.mean(eye)[:3]
            if avg_color[0]>avg_color[2]:
                color='Red'
            elif avg_color[1]>avg_color[0] and avg_color[1]>avg_color[2]:
                color='Green'
            else:
                color='Blue'
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.putText(roi_color,color,(ex,ey-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
            return frame 
        cap=cv2.VideoCapture(0)
        while True:
            ret,frame=cap.read()
            frame=detect_eyes(frame)
            cv2.imshow('Eye Detection',frame)
            
            if cv2.waitKey(1)& 0xFF == ord('q'):
                break 
            cap.release()
            cv2.destroyAllWindows()
            