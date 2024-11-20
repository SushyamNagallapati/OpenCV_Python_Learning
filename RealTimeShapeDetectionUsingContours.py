import cv2

import numpy as np

frame_width = 640
frame_height = 480

cap = cv2.VideoCapture(0) #--> If we enter "0" we can turn on the default webcam
cap.set(3, frame_width)
cap.set(4, frame_height)

def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 480)
cv2.createTrackbar("Threshold1", "Parameters", 70, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 64, 255, empty)
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale,scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


def getContours(image, imageContour):

    contours, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # cv2.RETR_EXTERNAL - Retrieves the outer corner of the Contour.
                                                                                             # cv2.RETR_TREE - Retrieves all the Contours and re-constructs full hierarchy
                                                                                             # cv2.CHAIN_APPROX_NONE - Used to get all the stored contour points
                                                                                             # cv2.CHAIN_APPROX_SIMPLE - This compresses the contour values and gives lesser number of points
                                                                                             # cv2.RETR_TREE - Retrieves all the Contours and re-constructs full hierarchy
                                                                                             # cv2.CHAIN_APPROX_NONE - Used to get all the stored contour points
                                                                                             # cv2.CHAIN_APPROX_SIMPLE - This compresses the contour values and gives lesser number of points
#Defining the Draw Area
    for contour in contours:
        area = cv2.contourArea(contour)
        areaMinimum = cv2.getTrackbarPos("Area", "Parameters")
        if area > areaMinimum:
            cv2.drawContours(imageContour, contour, contourIdx=-1, color=(255, 0 ,255), thickness=7) # cv2.drawContours - Used to draw the Contour ie, displays the output (imageContour)
#To get the length of the Contour we need to use the Arc Length
            perimeter = cv2.arcLength(curve=contour, closed=True) #Curve is the point, in which part the length to be taken. #Closed, represents the border is closed or not

            approximate = cv2.approxPolyDP(curve=contour, epsilon=0.02 * perimeter, closed=True)  #-> approxPolyDP is used to get the shape type
            print(len(approximate))

#To get the Bounding Area, this highlights the area around the shape, which we need.
            x, y, w, h = cv2.boundingRect(approximate)
            cv2.rectangle(img=imageContour, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=5) # cv2.rectangle is used to  draw a rectangle on the image Contour
                                                                                                            # pt1 = (x, y) are the initial points
                                                                                                            # pt2 = (x + w, y + h) says x + width, y + height denotes as the final corner of the Bounding Area (Square/Rectangle)

#To display values
            cv2.putText(imageContour, "Points: " + str(len(approximate)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2) #-> len(approximate) says the no. of end points to the shape
                                                                                                                                                                          #-> org: (x + w + 20, y + 20) is the initial position

            cv2.putText(imageContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2) #-> same as above but, int(area) is used to give integer values instead of float


while True:
    sucess,image = cap.read()
    imageContour = image.copy()

    imageBlur = cv2.GaussianBlur(image, (7, 7), 0)
    imageGray = cv2.cvtColor(imageBlur, cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")

    imageCanny = cv2.Canny(imageGray, threshold1, threshold2)

    kernel = np.ones((5, 5), np.uint8)
    imageDilation = cv2.dilate(imageCanny, kernel, iterations=1) # Dilation function is used to reduce the overlaps and noise in the video

    getContours(imageDilation, imageContour)

    imageStack = stackImages(0.8, ([image, imageGray, imageCanny],
                                   [imageDilation, imageContour, imageContour]))

    cv2.imshow("Result", imageStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


