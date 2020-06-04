import imutils
import cv2
img=cv2.imread("images.jpeg")
#height,width and depth of image
(h,w,d)=img.shape
print(h,w,d)
cv2.imshow("Real image",img)
#extracting region of interest from the image
roi=img[10:50,10:50]
cv2.imshow("region of interest",roi)
#resizing images
resized=cv2.resize(img,(100,100))
cv2.imshow("resized image",resized)
#calculating the aspect ratio and using it to resize the image lets resize the width to be 300 px but calculate height to use
r=300/w
dim=(300,int(h*r))
resized=cv2.resize(img,dim)
cv2.imshow("im",resized)
#doing this using imutils module
resized=imutils.resize(img,width=300)
cv2.imshow("resized using imutils",resized)
#rotating an image
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,-45,1.0)
rotated=cv2.warpAffine(img,M,(w,h))
cv2.imshow("rotated image using opencv",rotated)
#rotation using imutils
rotated=imutils.rotate(img,-45)
cv2.imshow("rotated image using imutils",rotated)
#to rotate image without clipping and without out of view after rotation
rotation=imutils.rotate_bound(img,45)
cv2.imshow("rotation of image without clipping",rotation)
#smoothing and image
blurred=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow("blurred image",blurred) 
cv2.waitKey(0)
