# First we collect data from sensor from data module
# From depth image we get color_image and depth
# Tyo color imgae ma ako lai object detection ma pass garni
# Object detection bata ako boundry box ma if manxeya x vanya (person) ani teslai face recognition ma pass garni.

import cv2
import numpy as np



from data import camerasensro
from object_detection import detection
from object_tracking import objects_tracking
from image_depth import depth
from faces_recognition import face_recog





sensordata = camerasensro.Sensordata()
object_detec = detection.Detection()
object_tracking = objects_tracking.CentroidTracker()
face_reco = face_recog.Faces_recognition()
face_reco.traning()

while True:
    color_image,depth_colormap,combine_image = sensordata.get_sensor_data()
    detected_response = object_detec.detection(color_image)
    
    rects = []
    for object in detected_response:
        
        # Object detection result
        Object_detection_result = '%s: %d%%' % (object["object_name"], int(object["confidence_score"])) # Example: 'person: 72%'
        


        # Depth calculation result
        box = [object["xmin"],object["ymin"],object["xmax"],object["ymax"]]
        box = np.array(box)
        rects.append(box.astype("int"))
        hist, dept = depth.get_hist_depth(depth_colormap,box)
        
        # Face recognition result
        crop_img = color_image[object["ymin"]:object["ymax"], object["xmin"]:object["xmax"]]
        y1, x2, y2, x1, name = face_reco.inference(crop_img)
        

        # Display all things
        finaltext = Object_detection_result + ", depth :" + str(dept) + ", name:" + name
        labelSize, baseLine = cv2.getTextSize(finaltext, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2) # Get font size
        label_ymin = max(object["ymin"], labelSize[1] + 10) # Make sure not to draw label too close to top of window
        cv2.rectangle(color_image, (object["xmin"],object["ymin"]), (object["xmax"],object["ymax"]), (10, 255, 0), 2)
        cv2.rectangle(color_image, (object["xmin"], label_ymin-labelSize[1]-10), (object["xmin"]+labelSize[0], label_ymin+baseLine-10), (255, 255, 255), cv2.FILLED) # Draw white box to put label text in
        cv2.putText(color_image, finaltext, (object["xmin"], label_ymin-7), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1) # Draw label text

    # Object tracking
    objects = object_tracking.update(rects)
    # loop over the tracked objects
    for (objectID, centroid) in objects.items():
        # draw both the ID of the object and the centroid of the
        # object on the output frame
        text = "ID {}".format(objectID)
        cv2.putText(color_image, text, (centroid[0] - 10, centroid[1] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(color_image, (centroid[0], centroid[1]), 4, (0, 255, 0), -1)
            
                
    cv2.namedWindow('RealSense', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Object detector',color_image)
    cv2.waitKey(1)
