import cv2
import pytesseract as tess
import os

path=r'D:\MOVIE\darkflow\darkflow-master\task-2'

li=[]
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

di=os.listdir(path)
print(len(di))

for i in range(len(di)):
    filename=os.path.join(path,di[i])
    img=cv2.imread(filename)
    crop=img[10:110,1400:1800]

    gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    #img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    ref=cv2.medianBlur(thresh,5)
    #print(img.shape)

    cv2.imshow("image1", thresh)


    result=tess.image_to_string(ref)
    final=result[1:3]+result[4:
    print(result)

    #cv2.imshow('image',crop)
cv2.waitKey(0)

'''

img=cv2.imread('frame_27.jpg')
crop=img[10:110,1400:1800]

cv2.imshow('image',crop)

'''
