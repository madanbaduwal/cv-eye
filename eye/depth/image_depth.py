import numpy as np
import cv2


def apply_filter(input):
    # application of filter
    filtered = input
    return filtered

def get_hist_depth(depth_array, box):
    """returns the histogram and depth of the ROI in given depth image
    Args:
        depth_array (2-d image array): Grayscale image 16-bit
        box (array<int>): [x1, y1, x2, y2]
    Returns:
        histogram, depth(mm): histogram array and depth of ROI in image is returned respectively
    """

    x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
    depth_array_roi = depth_array[y1:y2, x1:x2]
    roi_array = depth_array_roi
    img = apply_filter(roi_array)

    # depth_array_blur = cv2.GaussianBlur(img, (5,5), 5)
    # print(img)
    depth_array_blur = cv2.GaussianBlur(img, (3,3), 3)
    depth_array_blur = img

    depth_array_hist = np.histogram(depth_array_blur, bins=100, range=(100,5000))
    # print(depth_array_hist)

    hist = (depth_array_hist[0], depth_array_hist[1][0:-1])
    val = max(hist[0])
    index = np.where(hist[0] == val)
    depth = hist[1][index][0]
    return hist, depth

def visualize(depth_array, roi):
    # Drawing region of interest
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_array, alpha=0.03), cv2.COLORMAP_JET)
    cv2.rectangle(depth_colormap, tuple(roi[0:2]), tuple(roi[2:4]), 0, thickness=2)

    figure_image = depth_array
    cv2.rectangle(figure_image, tuple(roi[0:2]), tuple(roi[2:4]), 60000, thickness=1)

    # show images
    cv2.imshow("region", figure_image)
    cv2.imshow("color", depth_colormap)
    cv2.waitKey(100)
    
    
    
