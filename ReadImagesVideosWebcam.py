import cv2

# To view Images
image = cv2.imread("Resources/opencvTI.png")

cv2.imshow("Sushyam", image)

cv2.waitKey(0)

# To play a Video
frameWidth = 600
frameHeight = 300

cap = cv2.VideoCapture("Resources/testvideo.mp4") #--> If we enter "0" we can turn on the default webcam
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    sucess,img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
      
