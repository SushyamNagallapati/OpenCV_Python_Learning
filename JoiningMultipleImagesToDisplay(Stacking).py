import cv2
import numpy as np
from StackingImagesTest import stackImages

# img1 = cv2.imread("Resources/opencvTI.png", 0)
# img2 = cv2.imread("Resources/Road.jpg")
#
# width, height = 335, 360
#
# image2Resize = cv2.resize(img2, (height, width))
# print(img1.shape)
# print(image2Resize.shape)
#
# imgGray = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)
#
# image1 = cv2.resize(imgGray,(0, 0), None, 0.5, 0.5)
# image2 = cv2.resize(image2Resize,(0, 0), None, 0.5, 0.5)
#
# horizontal = np.hstack((image1, image2))
# vertical = np.vstack((image1, image2))
#
# stackedImages = stackImages(1, ([image1, image2]))
# cv2.imshow("StackedImages", stackedImages)
#
# cv2.imshow("Horizontally Stacked Image", horizontal)
# cv2.imshow("Vertically Stacked Image", vertical)
#
# cv2.waitKey(0)


frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0) #--> If we enter "0" we can turn on the default webcam
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    sucess,img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    # cv2.imshow("Video", img)

    kernel = np.ones((5, 5), np.uint8)
    print(kernel)

    #path = "Resources/opencvTI.png"

    #image = cv2.imread(path)

    imageGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imageBlur = cv2.GaussianBlur(imageGray,(7, 7), 0)

    imageCanny = cv2.Canny(imageBlur, 20, 20)

    imageDilation = cv2.dilate(imageCanny, kernel, iterations=1)

    imageEroded = cv2.erode(img, kernel, iterations=2)

    # imageBlank = np.zeros((5,5), np.uint8) #-> We can use this for a blank image

    stackedImages =  stackImages(0.8,([img, imageGray, imageBlur], [imageCanny, imageDilation, imageEroded]))
    cv2.imshow("Stacked Images", stackedImages)


    # cv2.imshow("Image", img)
    # cv2.imshow("ImageGray", imageGray)
    # cv2.imshow("ImageBlur", imageBlur)
    # cv2.imshow("ImageCanny", imageCanny)
    # cv2.imshow("ImageDilation", imageDilation)
    # cv2.imshow("ImageEroded", imageEroded)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
