import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "/home/aditya/College Project/Dataset"

def getImageswithId(path):
    ImagePaths,faces,ids = [],[],[]
    for users in os.listdir(path):
        actual_path = os.path.join(path,users)
        ImagePaths.extend([os.path.join(actual_path,f) for f in os.listdir(actual_path)])

        ids.append(int(users[-1]))

    for imagePath in ImagePaths:
        faceImg = Image.open(imagePath)
        faceNp = np.array(faceImg,"uint8")
        faces.append(faceNp)


    ids = ids*len(faces)
    return (ImagePaths,np.array(ids),np.array(faces))

path, ids, faces = getImageswithId(path)
recognizer.train(faces,ids)
recognizer.save("recognizer/trainingData.yml")
