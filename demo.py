import cv2
SRC = 'yuantu.jpg'
img_rgb = cv2.imread(SRC)
# cv2.imshow('rgb', img_rgb) # 原图
# cv2.waitKey(0)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', img_gray) # 灰度图
# cv2.waitKey(0)
img_blur = cv2.GaussianBlur(img_rgb, ksize=(21, 21), sigmaX=0, sigmaY=0)
cv2.imshow('img_blur', img_blur) # 高斯虚化
cv2.waitKey(0)
cv2.imwrite('hh.jpg', img_blur)
# img_blend = cv2.divide(img_gray, img_blur, scale=255)
# cv2.imshow('img_blend', img_blend) # 素描
# cv2.waitKey(0)
# cv2.imwrite('哈哈.jpg', img_blend)