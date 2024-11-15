import cv2

path = "Resources/Road.jpg"

image = cv2.imread(path)

width, height = 1000, 1000

# How to resize an image
imageResize = cv2.resize(image,(width, height))
print(image.shape)
print(imageResize.shape)

# How to crop an image
imageCropped = imageResize[700:1920, 420:550]
print(imageCropped.shape)

#How to resize the cropped image output to the original size
imageCropResize = cv2.resize(imageCropped, (image.shape[1], image.shape[0]))
print(imageCropResize.shape)

cv2.imshow("OriginalSize", image)
cv2.imshow("ImageResize", imageResize)
cv2.imshow("ImageCrop", imageCropped)
cv2.imshow("ImageCropResize", imageCropResize)

