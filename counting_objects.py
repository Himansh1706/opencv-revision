import cv2
import imutils
import argparse
#constructing argument parser and parse the arguments
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True)
args=vars(ap.parse_args())
image=cv2.imread(args["image"])

#convert image to gray scale 
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray",gray)
#cv2.waitKey(0)
#edge detection
edged=cv2.Canny(gray,30,150)
# cv2.imshow("edged",edged)
# cv2.waitKey(0)
#thresholding
thresh=cv2.threshold(gray,225,255,cv2.THRESH_BINARY_INV)[1]
#finding contours i.e. outlines of the foreground images in the threshold image
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
output=image.copy()
for c in cnts:
    cv2.drawContours(output,[c],-1,(240,0,159),3)
    #cv2.imshow("contours",output)
    #cv2.waitKey(0)
# draw the total number of contours found in purple
text = "I found {} objects!".format(len(cnts))
cv2.putText(output, text, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX, 0.7,
	(240, 0, 159), 2)
cv2.imshow("Contours", output)
cv2.waitKey(0)