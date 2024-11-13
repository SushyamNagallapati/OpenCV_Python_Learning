import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)  #-> Kernel is a matrix, used to iterate through the image to perform a function.
                                          # (5,5) is the size of the matrix.
                                          # uint8: 8-bit unsigned integer (0 to 255). Most often this is used for arrays representing images,
                                          # with the 3 color channels having small integer values (0 to 255).
print(kernel)

path = "Resources/opencvTI.png"

image = cv2.imread(path)
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #-> The cv2.COLOR_BGR2GRAY is used change the image color to gray
imageBlur = cv2.GaussianBlur(imageGray,(7, 7), 0)  #-> The cv2.GaussianBlur blurs the given image.
                                                                # We should put only the odd numbers in ksize, it used to increase the bulrness of the image

imageCanny = cv2.Canny(imageBlur, 20, 20) #-> The cv2.Canny gives the edge of the given image

imageDilation = cv2.dilate(imageCanny, kernel, iterations=1) #-> The cv2.dilate adds more thickness(iterations) to the given image.
                                                             # Dilation expands the white regions in a binary image.
                                        # When you set iterations=1, the dilation applies once, expanding the edges based on the shape and size of the kernel.

imageEroded = cv2.erode(image, kernel, iterations=2) #-> The cv2.erode is used to thin(iterations) out the edges of the given image.
                                                     # Erode is the opposite of Dilation. Instead of expanding white regions, erosion shrinks them.

cv2.imshow("Image", image)
cv2.imshow("ImageGray", imageGray)
cv2.imshow("ImageBlur", imageBlur)
cv2.imshow("ImageCanny", imageCanny)
cv2.imshow("ImageDilation", imageDilation)
cv2.imshow("ImageEroded", imageEroded)

cv2.waitKey(0)
