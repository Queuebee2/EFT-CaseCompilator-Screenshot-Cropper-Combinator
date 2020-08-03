import cv2
import numpy as np
import os

INPUT_AND_OUTPUT_DIR = 'output'

""" Code from
https://note.nkmk.me/en/python-opencv-hconcat-vconcat-np-tile/

I  changed 'min' to max, that's all.

"""

def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = max(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

def hconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    h_min = max(im.shape[0] for im in im_list)
    im_list_resize = [cv2.resize(im, (int(im.shape[1] * h_min / im.shape[0]), h_min), interpolation=interpolation)
                      for im in im_list]
    return cv2.hconcat(im_list_resize)

def concat_tile(im_list_2d):
    return cv2.vconcat([cv2.hconcat(im_list_h) for im_list_h in im_list_2d])


# something wrong with this one, makes everything gray...
def concat_tile_resize(im_list_2d, interpolation=cv2.INTER_CUBIC):
    im_list_v = [hconcat_resize_min(im_list_h, interpolation=cv2.INTER_CUBIC) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v, interpolation=cv2.INTER_CUBIC)


images = []

for filename in os.listdir(INPUT_AND_OUTPUT_DIR):

    # dont wanna use the earlier output in the new one
    # cba to do this with an or, or a list atm.
    if filename in ["big long boi.png",
                    f'big long boi small.png',
                    f'big long boi smaller.png',
                    f'big long boi smallest.png']:
        print(f'skipping {filename} because thats an outputfile-name..')
        continue
    
    if filename.endswith(".png"):
        images.append(cv2.imread(f'{INPUT_AND_OUTPUT_DIR}//{filename}'))

image_of_concatenated_images = vconcat_resize_min(images)

"""
FIXED but still a todo
okay since nothing works...

- find largest image
- paste every smaller image onto a canvas filled with a background
- then concatenate vertically

	HTML/HEX code:	#151615	
RGB code:	rgb(21, 22, 21)

"""

status = cv2.imwrite(f'{INPUT_AND_OUTPUT_DIR}//big long boi.png', image_of_concatenated_images)

if status:
    print('success!')
else:
    print('no succes!! :(')


print('resizing... 50%')

resize1 = cv2.resize(image_of_concatenated_images, (0,0), 0.5, 0.5, cv2.INTER_AREA)
status = cv2.imwrite(f'{INPUT_AND_OUTPUT_DIR}//big long boi small.png', image_of_concatenated_images)


if status:
    print('success!')
else:
    print('no succes!! :(')


print('resizing...25% ')

"""
issue OpenCV resize fails on large image with “error: (-215) ssize.area() > 0 in function cv::resize”
https://stackoverflow.com/questions/31996367/opencv-resize-fails-on-large-image-with-error-215-ssize-area-0-in-funct

resize1 = cv2.resize(image_of_concatenated_images, (0,0), 0.25, 0.25)
status = cv2.imwrite(f'{INPUT_AND_OUTPUT_DIR}//big long boi smaller.png', image_of_concatenated_images)


if status:
    print('success!')
else:
    print('no succes!! :(')

print('resizing...10%')

resize1 = cv2.resize(image_of_concatenated_images, (0,0), 0.1, 0.1)
status = cv2.imwrite(f'{INPUT_AND_OUTPUT_DIR}//big long boi smallest.png', image_of_concatenated_images)


if status:
    print('success!')
else:
    print('no succes!! :(')
"""
print('erm nvm i changed my mind')
