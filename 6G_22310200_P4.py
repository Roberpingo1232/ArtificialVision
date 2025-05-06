import numpy as np
import cv2

img = cv2.imread('watch.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(180,165),(255,0,0),1)
cv2.rectangle(img,(10,13),(250,150),(0,0,255),15)
cv2.circle(img,(150,90), 50, (500,255,500), -1)
pts = np.array([[100,32],[50,70],[150,50],[110,30]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'LamineYamal',(0,100), font, 1.2, (100,255,200), 3, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
