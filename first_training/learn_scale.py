#This program is the first attempt to train a tensorflow (tf) model to read the scale off of an Image
#Values are the images themselves with an integrated scale (mumeter/px)
#labels is the scale in mumeter/px
#there will be an attempt to read the proprietary metadata of the microscopes images using https://github.com/tg12/script-toolbox/blob/main/exif_df.py

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import os

#test of metadata extraction
from exif_df import *


#read all data from ../../../images
#md_df = extract_metadata("../../../images/Mo Schliffbilder")
#print(md_df)
#cant extract metadata
image_dir = "../../../images/"
#load images
train_images = tf.keras.utils.image_dataset_from_directory(image_dir,
                                                           validation_split=0.2,
                                                           subset="training",
                                                           seed=123,
                                                           image_size=(2880, 2160))
validation_images = tf.keras.utils.image_dataset_from_directory(image_dir,
                                                                validation_split=0.2,
                                                                subset="validation",
                                                                seed=123,
                                                                image_size=(2880, 2160))
print("test")


#manually make labels :(
#train_labels = tf.data.Dataset.from(np.array([]))
