#!/usr/bin/env python
# coding: utf-8

# In[1]:Write your code to find the histogram of gray scale image and color image channels


import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread('img1.jpg')
color_image = cv2.imread('img2.jpg')
cv2.imshow("Gray image",gray_image)
cv2.imshow("color image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# In[2]:Display the histogram of gray scale image and any one channel histogram from color image


import matplotlib.pyplot as plt 
grayscale_image=cv2.imread("gray image of flower.jpg")
colourscale_image=cv2.imread("color image of flower.jpg")
hist=cv2.calcHist(grayscale_image,[0],None,[255],[0,255])
hist1=cv2.calcHist([color_img],[1],None,[256],[0,256])
plt.figure()
plt.imshow(gray_img)
plt.title("Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.stem(hist)
plt.show()



# In[3]:Write the code to perform histogram equalization of the image. 



import cv2
gray_img = cv2.imread('B&W.jpg',0)
gray_img = cv2.resize(gray_img,(300,200))
cv2.imshow('Grey Scale Image',gray_img)
equ = cv2.equalizeHist(gray_img)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)








