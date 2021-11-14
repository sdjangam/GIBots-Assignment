import cv2
import numpy as np

def intersect(b1, b2):
    x1, y1, w1, h1 = b1
    x2, y2, w2, h2 = b2
    return x2 + w2 > x1 > x2 - w1 and y2 + h2 > y1 > y2 - h1

np.random.seed(55)
boxes = np.random.randint(2, 150, (2, 4, 2)) + np.random.randint(0, 300, (2, 4, 2))

bounds = [cv2.boundingRect(box) for box in boxes]
valids = [b1 for b1 in bounds if not any(intersect(b1, b2) for b2 in bounds if b1 != b2)]

img = np.zeros((500, 500), "uint8")
for x, y, w, h in bounds:
    cv2.rectangle(img, (x, y), (x + w, y + h), 255, 1)

if valids:
    x, y, w, h = max(valids, key=lambda b: b[2] * b[3])
    cv2.rectangle(img, (x, y), (x + w, y + h), 128, -1)

cv2.imshow("Bounding Box", img)
cv2.waitKey(0)