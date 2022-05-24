import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for x,y,w,h in faces:
        x1,y1=x+w, y+h
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,255), 2)
        cv2.line(img, (x,y), (x+30,y),(255,0,255), 12)
        cv2.line(img, (x,y), (x,y+30),(255,0,255), 12)
        
        cv2.line(img, (x1,y), (x1-30,y),(255,0,255), 12)
        cv2.line(img, (x1,y), (x1,y+30),(255,0,255), 12)
        
        cv2.line(img, (x,y1), (x+30,y1),(255,0,255), 12)
        cv2.line(img, (x,y1), (x,y1-30),(255,0,255), 12)
        
        cv2.line(img, (x1,y1), (x1-30,y1),(255,0,255), 12)
        cv2.line(img, (x1,y1), (x1,y1-30),(255,0,255), 12)
        
    cv2.imshow("img", img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
     break

cap.release()
    