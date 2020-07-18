import pytesseract as tess
import cv2
import numpy as np

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img=cv2.imread('y.jpg')
#img=cv2.resize(img,(1100,1100))
#img=img[50:250,135:250]


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

#img[thresh == 255] = 0

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
erosion = cv2.erode(img, kernel, iterations = 1)
#ref=cv2.filter2D(img,-2,kernel)
#ref=cv2.Canny(ref,100,200)
#ref=cv2.medianBlur(ret,5)
#ref=cv2.blur(thresh,(5,5))
#ref= cv2.bilateralFilter(thresh,9,75,75)
#ref=cv2.GaussianBlur(thresh,(5,5),0)

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image1", thresh)
#cv2.imshow("image", erosion)
#cv2.imshow("image2", ref)
#cv2.imshow("image", ref)

result=tess.image_to_string(thresh)
print(result)
print(result[4:8])

cv2.waitKey(0)
cv2.destroyAllWindows()

#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#img=cv2.resize(img,(950,950))

#kernel=np.zeros((4,4),np.uint8)

#dilation=cv2.dilate(img,kernel,iterations=2)
#ref = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)
#ref=cv2.filter2D(img,-2,kernel)
#ref=cv2.Sobel(img,cv2.CV_64F,1,0)
#ref1=cv2.Sobel(ref,cv2.CV_64F,0,1)
#ref=cv2.Canny(img,100,200)

#cv2.imshow('image',img)
#cv2.imshow('image',ref)

