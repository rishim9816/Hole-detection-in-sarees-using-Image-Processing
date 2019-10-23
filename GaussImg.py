import cv2
import numpy as np

#take image input and convert to grayscale
img = cv2.imread("C:\\Users\\Rishi Mukherjee\\Desktop\\wow.jpg",1);
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# take the gaussian blur image
gauss = cv2.GaussianBlur(img,(5,5),100)

#find threshold to convert into pure black white image
ret,thresh = cv2.threshold(gauss,127,255,0)

#detect holes using blob detector
detector = cv2.SimpleBlobDetector_create()
keypoint = detector.detect(thresh);
imgkeypoint = cv2.drawKeypoints(thresh,keypoint,np.array([]),(0,255,0),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

#show the image on to the screen
cv2.imshow("legend",imgkeypoint);
cv2.waitKey(0)
cv2.destroyAllWindows()