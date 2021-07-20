# In this module we do object detection and render it in streamlit web app

# import the necessary packages
from edgetpu.detection.engine import DetectionEngine
from imutils.video import VideoStream
from PIL import Image
import argparse
import mina.config as settings
import imutils
import time
import cv2


class ObjectDetection:
    def __init__(self):
        self.args = {}
        self.args["confidence"] = 0.3

    def detect_object(self, image_path):
        """ Object detection using coral tpu. This function enforce to have tpu on your system.

        Args :

        Return :
                image (): image frame with boundry box
                label (str): label of the boundry box 

        """
        self.args["labels"] = settings.pretrained_object_detection_classes
        self.args["model"] = settings.pretrained_object_detection_model
        self.labels = {}
        for row in open(self.args["labels"]):
            (classID, label) = row.strip().split(maxsplit=1)
            self.labels[int(classID)] = label.strip()
        self.model = DetectionEngine(self.args["model"])
        frame = cv2.imread(image_path)
        results = self.model.detect_with_image(frame, threshold=self.args["confidence"],
                                               keep_aspect_ratio=True, relative_coord=False)
        whole_response = []
        for r in results:
            response = {}
            response['box'] = r.bounding_box.flatten().astype("int")
            response['label'] = self.labels[r.label_id]
            response['confidence'] = r.score
            whole_response.append(response)
        return whole_response
