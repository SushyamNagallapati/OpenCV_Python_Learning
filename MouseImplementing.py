import cv2
import numpy as np

# Initialize Variables
circles = np.zeros((4, 2), np.int32)
counter = 0

# Define the Mouse Call Back Function
def mouseClick(event, x, y, flags, parameters):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x, y
        counter = counter + 1
        print(circles)

# Read the Image
image = cv2.imread("Resources/Cards.jpg")

while True:

    if counter == 4:
        width, height = 250, 350
        point1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
        point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
        matrix = cv2.getPerspectiveTransform(point1, point2)
        output = cv2.warpPerspective(image, matrix, (width, height))
        cv2.imshow("Output Image", output)

    for i in range(0, 4):
        cv2.circle(image, (int(circles[i][0]), int(circles[i][1])), 3, (0, 255, 0), cv2.FILLED)


    cv2.imshow("Original Image", image)
    cv2.setMouseCallback("Original Image", mouseClick)
    cv2.waitKey(1)
# cv2.destroyAllWindows()  #-> Prevents Freezing, Clean Resource Management


