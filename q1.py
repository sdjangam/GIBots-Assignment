import cv2
 
image = cv2.imread('AutoCAD_Sample.png')
 
cv2.circle(image,(1, 0), 25, (0,255,0))
cv2.circle(image,(2, -7), 25, (0,0,255))
cv2.circle(image,(8, 1), 25, (0,255,0))
cv2.circle(image,(9, -6), 25, (0,0,255))
 
cv2.imshow('points are not lying on the same circle',image)
cv2.waitKey(0)
cv2.destroyAllWindows()