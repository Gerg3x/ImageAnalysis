import cv2

#Image path
image_path = r'C:\Users\Trainees\Desktop\image.jpg'
#Read Image
img = cv2.imread(image_path)
#Create an SR object
sr = cv2.dnn_superres.DnnSuperResImpl_create()
#Read the model
path = r"C:\Users\Trainees\Desktop\EDSR_x2.pb"
#path = r"C:\Users\Trainees\Desktop\EDSR_x4.pb"
sr.readModel(path)
#Set the desired model and scale to get correct pre- and post-processing
sr.setModel("edsr", 2)
#sr.setModel("EDSR", 4)
#Upscale the image
result = sr.upsample(img)
# Save the image
cv2.imwrite("./upscaled.png", result)


