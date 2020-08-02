# Author :    Queuebee2
# Date   :    3-8-2020

import os
import sys
import cv2
import numpy as np


"""

███████╗███████╗████████╗████████╗██╗███╗   ██╗ ██████╗ ███████╗
██╔════╝██╔════╝╚══██╔══╝╚══██╔══╝██║████╗  ██║██╔════╝ ██╔════╝
███████╗█████╗     ██║      ██║   ██║██╔██╗ ██║██║  ███╗███████╗
╚════██║██╔══╝     ██║      ██║   ██║██║╚██╗██║██║   ██║╚════██║
███████║███████╗   ██║      ██║   ██║██║ ╚████║╚██████╔╝███████║
╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                                                                
"""

# the directory with the selection of screenshots you want to crop
# In windows you'll have to change every "/" to a "//" to 'escape' them
INPUT_FILES_FOLDER = "input"

# the output directory for cropped screenshots
# In windows you'll have to change every "/" to a "//" to 'escape' them
OUTPUT_FILES_FOLDER = "output"

# Want a quick slideshow?
SHOW_IMAGES_ON_RUN = False


# if your resolution doesnt work, try cropping your desired
# upper_left and lower_right corners for the crop-area and
# setting them here.
# The image Files should be in the script directory.
UPPER_LEFT_CORNER = 'corner_upper_left.png'
LOWER_RIGHT_CORNER = 'corner_lower_right.png'

method = cv2.TM_SQDIFF_NORMED

for index, filename in enumerate(os.listdir(INPUT_FILES_FOLDER)):
   if filename.endswith(".png"):

      file_path = f'{INPUT_FILES_FOLDER}//{filename}'
      print((25*"-"))
      print(f"hocus pocus pilatus {filename[:25]}...")

      # Read the images from the files
      crop_corner_1 = cv2.imread(LOWER_RIGHT_CORNER)
      crop_corner_2 = cv2.imread(UPPER_LEFT_CORNER)
      the_whole_image = cv2.imread(file_path)

      # find the first corner (lower right)
      # by matching the corner picture on the big screenshot
      result_1 = cv2.matchTemplate(crop_corner_1, the_whole_image, method)

      # We want the minimum squared difference blabla idk how this works
      # exactly. It does some searchy-search and then we hope to get
      # the right location for the corner we're looking for
      mn,_,coordinates,_ = cv2.minMaxLoc(result_1)

      # Extract the coordinates of our best match
      LowerRightX,LowerRightY = coordinates

      # get the size of our corner, to add to the crop-area
      cornersize_y, cornersize_x = crop_corner_1.shape[:2]

      corner_1_coordX = LowerRightX + cornersize_x
      corner_1_coordY = LowerRightY + cornersize_y

      # aaand do everything again with the other corner
      result_2 = cv2.matchTemplate(crop_corner_2, the_whole_image, method)
      mn,_,coordinates2,_ = cv2.minMaxLoc(result_2)
      corner_2_coordX, corner_2_coordY  = coordinates2

      # now we crop the image
      target_region_img = the_whole_image[corner_2_coordY:corner_1_coordY, corner_2_coordX:corner_1_coordX]

      # give the file a name
      output_name = f"{OUTPUT_FILES_FOLDER}//{index} cropped {filename}.png"

      # try and save it (store true/false based on if it saved correctly)
      saved_status = cv2.imwrite(output_name, target_region_img)

      # show images as they're being cropped
      if SHOW_IMAGES_ON_RUN:
         cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE);
         cv2.imshow("image", target_region_img);
         cv2.waitKey(1)

      #  print according to save status
      if saved_status:
         #region ({corner_2_coordY}:{corner_1_coordY}, {corner_2_coordX}:{corner_1_coordX})
         print(f'saved region to {output_name}')
      else:
         print(f'could not save {output_name[:15]}')


