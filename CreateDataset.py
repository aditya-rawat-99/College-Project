import cv2
import os
max_sample = 2000

def create_dataset(intruder = False):
    face_cascade = cv2.CascadeClassifier("/home/aditya/College Project/data/haarcascade_frontalface_alt2.xml")
    cap = cv2.VideoCapture(0)

    id = input("Enter user ID: ")

    sampleNum = 0
    folder = "Dataset"
    if intruder:
        folder = "Unknown"
        max_sample = 1

    os.mkdir(folder +"/user" + str(id))
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

        for (x, y, w, h) in faces:
            cv2.imwrite("/home/aditya/College Project/" + folder + "/user"+str(id)+"/"+str(sampleNum)+".jpg",
                        gray[y:y+h, x:x+w])

            if intruder:
                if os.path.exists("/home/aditya/College Project/static/" + str(sampleNum) + ".jpg"):
                    os.remove("/home/aditya/College Project/static/" + str(sampleNum) + ".jpg")

                cv2.imwrite("/home/aditya/College Project/static/" + str(sampleNum) + ".jpg",gray[y:y + h, x:x + w])
                cap.release()
                cv2.destroyAllWindows()

                return

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            sampleNum += 1
            cv2.waitKey(100)


        cv2.imshow("frame", frame)
        cv2.waitKey(1)
        print(max_sample)
        if sampleNum == max_sample:
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    create_dataset(False)
