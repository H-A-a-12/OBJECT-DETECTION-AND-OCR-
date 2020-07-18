import cv2

def clicl_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,':',y)
        font=cv2.FONT_HERSHEY_COMPLEX
        strxy=str(x)+','+str(y)
        cv2.putText(img,strxy,(x,y),font,2,(255,0,0),2)
        cv2.imshow('image',img)

img=cv2.imread('frame_27.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',clicl_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
