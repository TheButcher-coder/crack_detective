#blends multiple masks into one singular using the following colors:

# metal = Gray 125, 125, 125
# sediment = Black 0, 0, 0
# Pore = Red 255, 0, 0
# crack = Blue 0, 255, 0

import numpy as np
from matplotlib.image import imread


colors = np.array([[125, 125, 125],
                      [0, 0, 0],
                      [255, 0, 0],
                      [0, 255, 0]])

#load all images
#naming convention:
#   task-[num]-annotation-[num]-by-1-tag-[maskname]-0.png
mask_names = np.array(['metal', 'sediment', 'Crack', 'Pore'])

#current max masks:
n = int(colors.size/3.0)     # =mask_names.size

#size of images:
sx = 2160; sy = 2880

#function to blend all masks into one
def blend_masks(mask_num):
    #first read all masks with corresponding number
    #construct name array
    file_names = []

    for i, name in enumerate(mask_names):
        file_names.append('../images/masks/' + 'task-' + str(mask_num) + '-annotation-' + str(mask_num) + '-by-1-tag-' + str(name) + '-0.png')

    #open all files into biiiig array
    temp = np.zeros((n, sx, sy))
    for i in range(n):
        try:
            print("[DEBUG]OPENING FILE: " + file_names[i])
            temp[i] = imread(file_names[i])
        except:
            print("[ERROR]COULD NOT OPEN FILE! Skipping: " + file_names[i])

    #blend all colors together


#test = imread('../images/masks/' + 'task-' + str(1) + '-annotation-' + str(1) + '-by-1-tag-' + str("metal") + '-0.png')
blend_masks(1)