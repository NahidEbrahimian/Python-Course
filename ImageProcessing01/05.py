import numpy as np
import cv2

# img = cv2.imread("image path")
img = np.ones([800, 600])

bar_position = img.shape[1] // 3
bar_width = bar_position // 3

for i in range(bar_position):
    if i > bar_position - bar_width:
        for j in range(0, bar_position - i):
                img[i, j] = 0
    else:
        for j in range(bar_position - bar_width - i, bar_position - i):
                img[i, j] = 0

cv2.imwrite('output/img.jpg', img*255)
cv2.imshow('img', img)
cv2.waitKey()