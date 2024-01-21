import cv2
#Configurable parameters
scale_percent=50
source= "source.jpg"
destination="new2.png"
src=cv2.imread(source,cv2.IMREAD_UNCHANGED)

cv2.imshow("title",src)
#percent by which the image is resized
#calculate the 50 % of original dimentions

width=int(src.shape[1]*scale_percent/100)
height=int(src.shape[0]*scale_percent/100)
dsize=(width,height)
#resize image

output=cv2.resize(src,dsize)

cv2.imwrite(destination,output)
cv2.waitKey(0)
