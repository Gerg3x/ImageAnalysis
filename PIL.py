
from PIL import Image, ImageEnhance, ImageFilter
from pyzbar.pyzbar import decode

def preprocess_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Convert the image to grayscale
        img = img.convert('L')
        # Upscaling
        x, y = img.size
        img = img.resize((int(round(x * 2)), int(round(y * 2))))
        #Sharpening
        img = ImageEnhance.Sharpness(img).enhance(1.5)
        # Increase contrast
        img = ImageEnhance.Contrast(img).enhance(1.2)
        #Enhance brightness
        #img = ImageEnhance.Brightness(img).enhance(1.5)
        #Apply Gaussian blur
        #img = img.filter(ImageFilter.GaussianBlur(radius=2))

        return img


def read_barcode(image_path):
    # Preprocess the image
    preprocessed_img = preprocess_image(image_path)

    # Decode barcodes
    barcodes = decode(preprocessed_img)

    if barcodes:
        for barcode in barcodes:
            # Barcode data and type
            barcode_data = barcode.data.decode('utf-8')
            barcode_type = barcode.type

            print(f"Type: {barcode_type}, Data: {barcode_data}")
    else:
        print("No barcode found in the image.")


# Replace 'path_to_your_image.jpg' with the path to your image file
image_path = r'C:\Users\Trainees\Desktop\image3.jpg'
preprocess_image(image_path)
read_barcode(image_path)
#Displays the preprocessed image using Image
preprocess_image(image_path).show()


