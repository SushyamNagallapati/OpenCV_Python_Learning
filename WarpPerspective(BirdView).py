import cv2
import numpy as np

image = cv2.imread("Resources/Cards.jpg")

width, height = 250, 350
# Writing the Matrix to Map the Card border
point1 = np.float32([[139, 262], [313, 242], [105, 464], [321, 431]])
point2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])  #-> Defining the point to print

matrix = cv2.getPerspectiveTransform(point1, point2)

output = cv2.warpPerspective(image, matrix, (width, height))

# print(point1)

for i in range(0, 4):
    cv2.circle(image, (int(point1[i][0]), int(point1[i][1])), 5, (255, 0, 0), cv2.FILLED)


cv2.imshow("Original Image", image)
cv2.imshow("Output Image", output)
cv2.waitKey(0)
cv2.destroyAllWindows()  #-> Prevents Freezing, Clean Resource Management
