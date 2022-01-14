

import cv2  
filename='\\...'
cap = cv2.VideoCapture(filename)
#de
x=0 
y=0 
w=650 
h=750

success, frame = cap.read()

while success :
    success, frame = cap.read()
        
    if success:
        cropeedIMAGE = frame[y:y+h, x:x+w]
        cv2.imshow('finger', cropeedIMAGE)
        
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()

