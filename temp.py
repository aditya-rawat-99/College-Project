from PIL import Image
import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier("/home/aditya/College Project/data/haarcascade_frontalface_alt2.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

path = "/home/aditya/Documents/personal documents/College/IMG-20190918-WA0065.jpg"

pil_image = Image.open(path).convert("L")
image_array = np.array(pil_image, "uint8")

faces = face_cascade.detectMultiScale(image_array, 1.2,5)

img = cv2.imread(path)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()