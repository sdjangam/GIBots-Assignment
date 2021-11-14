import numpy as np
import cv2

width = 100
height = 100


img = np.zeros((height, width, 3), np.uint8)


p1 = (1, 0)
p2 = (2, -7)
p3 = (8, 1)
p4 = (9, -6)
p5 = (8, 2)
p6 = (7, -7)
p7 = (8, -7)


cv2.line(img, p1, p2, (255, 0, 0), 7)
cv2.line(img, p2, p3, (255, 0, 0), 7)
cv2.line(img, p3, p4, (255, 0, 0), 7)
cv2.line(img, p4, p5, (255, 0, 0), 7)
cv2.line(img, p5, p6, (255, 0, 0), 7)
cv2.line(img, p6, p7, (255, 0, 0), 7)
cv2.line(img, p1, p7, (255, 0, 0), 7)



centroid = ((p1[0]+p2[0]+p3[0]+p4[0]+p5[0]+p6[0]+p7[0])//7, (p1[1]+p2[1]+p3[1]+p4[1]+p5[1]+p6[1]+p7[1])//7)


cv2.circle(img, centroid, 4, (0, 255, 0))


cv2.imshow("Triangle", img)
cv2.waitKey(0)
