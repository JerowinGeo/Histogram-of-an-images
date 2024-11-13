# Histogram-of-an-images


## Aim
To obtain a histogram for finding the frequency of pixels in an Image with pixel values ranging from 0 to 255. Also write the code using OpenCV to perform histogram equalization.

## Software Required:
Anaconda - Python 3.7

## Algorithm:
### Step1:
Read the gray and color image using imread()

### Step2:
Print the image using imshow().



### Step3:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### step4:
Use calcHist() function to mark the image in graph frequency for gray and color image.

### Step5:
The Histogram of gray scale image and color image is shown.


## Program:

# Developed By: Jerowin Geo J A
# Register Number: 212223100016

### Input Grayscale Image and Color Image
```
import cv2
import matplotlib.pyplot as plt
gray_image = cv2.imread('img1.jpg')
color_image = cv2.imread('img2.jpg')
cv2.imshow("Gray image",gray_image)
cv2.imshow("color image",color_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
### Histogram of Grayscale Image and any channel of Color Image
```
import numpy as np
gray_image=cv2.imread('img1.jpg')
import matplotlib.pyplot as plt 
gray_hist=cv2.calcHist(gray_image,[0],None,[255],[0,255])
plt.figure(figsize=(10,6))
plt.subplot(1,2,1)
plt.imshow(gray_image)
plt.subplot(1,2,2)
plt.title("Histogram")
plt.xlabel("Grayscale value")
plt.ylabel("pixel count")
plt.stem(gray_hist)
plt.show()
```

### Histogram Equalization of Grayscale Image
```
import cv2
gray_image = cv2.imread("img1.jpg",0)
cv2.imshow('Grey Scale Image',gray_image)
equ = cv2.equalizeHist(gray_image)
cv2.imshow("Equalized Image",equ)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Output:
### Input Grayscale Image and Color Image

![image](https://github.com/user-attachments/assets/535bd756-b67d-4171-93a7-4b904fba9299)


### Histogram of Grayscale Image and any channel of Color Image

![image](https://github.com/user-attachments/assets/52d48392-d052-417e-b12e-5e292b813958)


### Histogram Equalization of Grayscale Image
![image](https://github.com/user-attachments/assets/7bc847cc-5579-44ca-a2d7-61b1b7fac024)



## Result: 
Thus the histogram for finding the frequency of pixels in an image with pixel values ranging from 0 to 255 is obtained. Also,histogram equalization is done for the gray scale image using OpenCV.

