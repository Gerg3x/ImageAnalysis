import cv2
from pyzbar.pyzbar import decode


def BarcodeReader(image):

    img = cv2.imread(image)

    # EDSR superresolution
    sr = cv2.dnn_superres.DnnSuperResImpl_create()
    # Read the model
    path = r"C:\Users\Trainees\Desktop\EDSR_x2.pb"
    sr.readModel(path)
    # Set the desired model and scale to get correct pre- and post-processing
    sr.setModel("edsr", 2)
    # Upscale the image
    img = sr.upsample(img)
    #Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Threshold the image using threshold OTSU
    ret, img = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


    # Decode the barcode image
    detectedBarcodes = decode(img)
    print(detectedBarcodes)
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

image = r'C:\Users\Trainees\Desktop\image8.jpg'
BarcodeReader(image)




