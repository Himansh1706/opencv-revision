import cv2
import imutils
import argparse
#constructing argument parser and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())
image=cv2.imread(args["iamge"])
cv2.imshow("Image",image)
cv2.waitKey(0)
#convert image to gray scale 
gray=cv2.cvtColor(iamge,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.waitKey(0)
#edge detection
edged=cv2.Canny(gray,30,150)
cv2.imshow("edged",edged)
cv2.waitKey(0)
#thresholding
