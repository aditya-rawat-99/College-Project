import cv2
import numpy as np
import os
# import CreateDataset, UploadToS3,s3_signed_url
# from s3_signed_url import  access_keys
# from NotifyUser import notify_user


face_cascade = cv2.CascadeClassifier("/home/aditya/College Project/data/haarcascade_frontalface_alt2.xml")
cap = cv2.VideoCapture(0)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("/home/aditya/College Project/trainner.yml")

id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
identity = "Unknown"

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        id,conf = recognizer.predict(gray[y:y+h,x:x+w])

        if id == 1:
            identity = "Aditya"

        # else:
        #     CreateDataset.create_dataset(intruder = True)
        #     bucket_key = UploadToS3.upload_to_s3()
        #     url = s3_signed_url.create_presigned_url(access_keys["BUCKET_NAME"],bucket_key)
        #     notify_user(url = url)

        cv2.putText(frame,identity,(x,y+h),font,0.55,(0,255,0,1))
    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()