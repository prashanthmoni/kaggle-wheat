# main file for global wheat detection
# Author: Prashanth Moni


# intitialisations
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, filters
from PIL import Image
import glob
import cv2
import os


# Paths
# training data
training_data = r'C:\Users\bm00157.INETPMTC\Documents\Personal\data science\kaggle\global wheat detection\global-wheat-detection\ train*.jpg'
print(training_data)
i = io.imread('\global-wheat-detection\\train\0a3cb453f.jpg')
io.imshow(i)
io.show()
# load images
"""image_list = []
for filename in glob.glob(training_data):
    im = Image.open(filename)
    image_list.append(im)
"""


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        if img is not None:
            images.append(img)
    return images


image_list = load_images_from_folder(training_data)
print(len(image_list))
