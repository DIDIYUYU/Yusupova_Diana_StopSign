import cv2
import numpy as np

from matplotlib import pyplot as plt

def process_image(image_path):

    img = image_path

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    stop_data = cv2.CascadeClassifier("stop_data.xml")
    found = stop_data.detectMultiScale(img_gray,minSize =(20, 20))
    amount_found = len(found)

    if amount_found != 0:

        for (x, y, width, height) in found:

            cv2.rectangle(img, (x, y),
                          (x + height, y + width),
                          (0, 255, 0), 5)
    plt.subplot(1, 1, 1)
    plt.imshow(img)
    plt.show()
    return img
