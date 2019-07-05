import cv2
import numpy as np

image=cv2.imread("WaldoBeach.jpg")
cv2.imshow("waldo? where are you?",image)
cv2.waitKey(0)

image2=cv2.imread("waldo.jpg")
cv2.imshow("i look like this. find me",image2)
cv2.waitKey(0)

result=cv2.matchTemplate(image,image2,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(result)

top_left=max_loc
bottom_right=(top_left[0]+50 ,top_left[1]+50)
cv2.rectangle(image,top_left,bottom_right,(0,0,255),5)
cv2.imshow("rectangle",cv2.rectangle(image,top_left,bottom_right,(0,0,255),5))
cv2.waitKey(0)
cv2.imshow("waldo",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

