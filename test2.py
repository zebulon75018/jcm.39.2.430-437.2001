import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('testcopy.png')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('template.png', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
#cv.imwrite("reslevel.png", (res).astype(np.uint8))  # Scale to 0-255 for proper saving
#quit()
#res = cv.matchTemplate(img_gray,template,cv.TM_CCORR_NORMED)
threshold = 0.97
#threshold = 254
loc = np.where( res >= threshold)
n= 0
for pt in zip(*loc[::-1]):
        crop_img = img_rgb[pt[1]:pt[1]+h, pt[0]:pt[0]+w]
        cv.imwrite("crop%d_%d.png" % ( pt[0], pt[1] ) ,crop_img)
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv.imwrite("res%d.png" % ( int(100*threshold)),img_rgb)
