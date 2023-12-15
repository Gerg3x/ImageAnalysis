##Information extracted from https://github.com/Sawera557/Image_Processing_with_OpenCV/blob/main/Image_Processing_Python_OpenCV.ipynb

import cv2
import numpy as np
from scipy.signal import convolve2d as conv2
from skimage import color, data, restoration



#Read Image
image = r'C:\Users\Trainees\Desktop\image3.jpg'
#Open Image in gray scale
img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
#Construct a new Generator with the default BitGenerator
rng = np.random.default_rng()
#Add PSF and convolved the image
psf = np.ones((1, 1)) / 500
img = conv2(img, psf, 'same')
#Add noise to the image
img_noisy = img.copy()
img_noisy += (rng.poisson(lam=10, size=img.shape) - 10) / 255

# Restore Image using Richardson-Lucy algorithm
deconvolved_RL = restoration.richardson_lucy(img_noisy, psf)

cv2.imshow("Original", img)
cv2.imshow("Noise", img_noisy)
cv2.imshow("Deconvolved", deconvolved_RL)
cv2.waitKey(0)
cv2.destroyAllWindows()