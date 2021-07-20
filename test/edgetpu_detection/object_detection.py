# In this module we do object detection and render it in streamlit web app

# import the necessary packages
from edgetpu.detection.engine import DetectionEngine
from imutils.video import VideoStream
from PIL import Image
import argparse
import imutils
import time
import cv2
import os

class Detection:
    def __init__(self):
        self.cwd = os.getcwd()
        print(self.cwd)
        self.args = {}
        self.args["labels"] = self.cwd+"./model_and_label/coco_labels.txt"
        self.args["model"] = "./model_and_label/mobilenet_ssd_v2_coco_quant_postprocess_edgetpu.tflite"
        self.args["confidence"] = 0.3
        self.labels = {}
        for row in open(self.args["labels"]):
            (classID, label) = row.strip().split(maxsplit=1)
            self.labels[int(classID)] = label.strip()
        self.model = DetectionEngine(self.args["model"])
        self.vs = VideoStream(src=0).start()
        time.sleep(2.0)

    def object_detection(self):
        """ Object detection using coral tpu. This function enforce to have tpu on your system.

        Args :

        Return :
                image (): image frame with boundry box
                label (str): label of the boundry box 

        """
        frame = self.vs.read()
        frame = imutils.resize(frame, width=500)
        image = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        results = self.model.detect_with_image(frame, threshold=self.args["confidence"],
                                               keep_aspect_ratio=True, relative_coord=False)
        for r in results:
            box = r.bounding_box.flatten().astype("int")
            (startX, startY, endX, endY) = box
            label = self.labels[r.label_id]
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          (0, 255, 0), 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            text = "{}: {:.2f}%".format(label, r.score * 100)
            cv2.putText(image, text, (startX, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        return image, label


if __name__ == "__main__":
    obj = Detection()
    while True:
        image, label = obj.object_detection()
        print(image, label)
