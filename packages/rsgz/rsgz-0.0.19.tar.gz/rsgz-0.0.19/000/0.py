import cv2 as cv

fp = r"C:\Users\Administrator\Desktop\0.png"
img = cv.imread(fp)
cv.imshow('imgzzz', img)
cv.waitKey(0)