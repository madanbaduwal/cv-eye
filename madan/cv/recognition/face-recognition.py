import os

import cv2
import numpy as np

import face_recognition


class FacesRecognition:
    def __init__(self):
        self.CWD_PATH = os.path.abspath(__file__)
        self.CWD_PATH = os.path.normpath(self.CWD_PATH + os.sep + os.pardir)
        self.images = []
        self.classNames = []
        self.training_path = self.CWD_PATH + "/Training_images"
        self.myList = os.listdir(self.training_path)
        self.encodeList = []

    def add_face(self, person_name, image):
        """ Function that add faces
        Args:
            person_name(str): Name of the person
            image(opencv image) : Opencv image
        """
        print(type(person_name))
        image_name = f'{person_name}.jpg'
        os.chdir(self.training_path)
        print(os.chdir(self.training_path))
        cv2.imwrite(image_name, image)

    def traning(self):
        """ Function that train faces
        Args:
            No arguments
        """
        for cl in self.myList:

            curImg = cv2.imread(f'{self.training_path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            self.encodeList.append(encode)

    def inference(self, image, y1=0, x2=0, y2=0, x1=0, name='facenotfound'):
        """ Function that inference image
        Args:
            image(cv image) : image take for inference
        Returns:
            imag(cv image): image
            y1, x2, y2, x1 : coordinate of the detected face
            name(str) : name of the person
        """
        imgS = cv2.resize(image, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(
            imgS, facesCurFrame,
        )
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(
                self.encodeList, encodeFace,
            )
            faceDis = face_recognition.face_distance(
                self.encodeList, encodeFace,
            )
            if faceDis is None:
                print('face does not match')
            else:
                matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        return y1, x2, y2, x1, name


if __name__ == '__main__':
    face = Faces_recognition()
    face.traning()