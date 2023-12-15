import cv2
from pyzbar.pyzbar import decode



# Make one method to decode the barcode
def BarcodeReader(image):
    #Read the image
    img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
    #Scaling the image
    img_scale = cv2.resize(img, None, fx = 2, fy = 2,  interpolation = cv2.INTER_LINEAR)
    #Threshold the image using threshold OTSU - best results between the three thresholds
    ret , img = cv2.threshold(img_scale,0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    #Threshold the image using adaptive gaussian threshold
    #img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                #cv2.THRESH_BINARY, 11, 3)
    # Gaussian blur and threshold using OTSU
    # img = cv2.GaussianBlur(img,(5,5), 0)
    # ret, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Decode the barcode image
    detectedBarcodes = decode(img)
    # If not detected then print the message
    if not detectedBarcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:

            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x - 10, y - 10),
                          (x + w + 10, y + h + 10),
                          (255, 0, 0), 2)

            if barcode.data != "":
                # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    # Display the image
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = r'C:\Users\Trainees\Desktop\image3.jpg'
BarcodeReader(image)