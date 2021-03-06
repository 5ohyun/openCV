import cv2
import sys

print(cv2.__version__)

img = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

if img is None :
    print("failed")
    sys.exit()


cv2.imwrite('cat_gray.png',img) 

cv2.namedWindow('image')
cv2.imshow('image',img)
cv2.waitKey()

cv2.destroyAllWindows('image')