from PIL import Image, ImageEnhance, ImageFilter
from pyzbar.pyzbar import decode
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import argparse
from pyzbar import pyzbar

# Replace 'path_to_your_image.jpg' with the path to your image file
image_path = r'C:\Users\Trainees\Desktop\image.jpg'


# Open image with OpenCV
img_input = cv.imread(image_path, cv.IMREAD_GRAYSCALE)

####
decoder = pyzbar.decode(img_input)

if len(decoder) != 0:
    for decoded in decoder:
        if decoded.type == 'QRCODE':
            # Get the bounding box location of the QR Code
            left, top, width, height = decoded.rect

            # Crop input image (add 10 pixels to each side)
            qrcode = img_input[top - 10: top + height + 10, left - 10: left + width + 10]

            # Rotate QR Code, if necessary
            if decoded.orientation is not None and decoded.orientation != 'UNKNOWN':
                if decoded.orientation == 'LEFT':
                    # Rotate by 90 degrees clockwise
                    qrcode = cv.rotate(qrcode, cv.ROTATE_90_CLOCKWISE)
                elif decoded.orientation == 'RIGHT':
                    # Rotate by 270 degrees clockwise
                    qrcode = cv.rotate(qrcode, cv.ROTATE_90_COUNTERCLOCKWISE)
                elif decoded.orientation == 'DOWN':
                    # Rotate by 180 degrees clockwise
                    qrcode = cv.rotate(qrcode, cv.ROTATE_180)


                # Open image
                cv.imshow("image", qrcode)
                cv.waitKey(0)
