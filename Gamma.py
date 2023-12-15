from __future__ import print_function
import numpy as np
import argparse
import cv2


def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

image = r'C:\Users\Trainees\Desktop\image3.jpg'
original = cv2.imread(image)
# loop over various values of gamma
for gamma in np.arange(0.0, 3.5, 0.5):
  # ignore when gamma is 1 (there will be no change to the image)
  if gamma == 1:
    continue
  # apply gamma correction and show the images
  gamma = gamma
  if not gamma==0.0:
    print(f"***************GAMMA CORRECTION VALUE = {gamma}***************")
    adjusted = adjust_gamma(original, gamma=gamma)
    cv2.putText(adjusted, "g={}".format(gamma), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    org = cv2.resize(original, (300, 400))
    adj = cv2.resize(adjusted, (300, 400))
    cv2.imshow("Original", org)
    cv2.imshow("Modified", adj)
    cv2.waitKey(0)