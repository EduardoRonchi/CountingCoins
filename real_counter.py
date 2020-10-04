# Program to count coins
import numpy as np
import cv2
import os

# Load an color image with opencv
img = cv2.imread('real_original.jpg')

# Print the image on screen
cv2.imshow('Original Image', img)

# Convert image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Print the image on screen
cv2.imshow('Gray Image', gray)

# Applying a Gaussian filter to blurr the image
blurred = cv2.GaussianBlur(gray, (17, 17), 0)

# Print the image on screen
cv2.imshow('Blurred Image', blurred)

# Finding the circles using HoughCircles function
circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1.5, 100)

# Drawing the circles and the centroids
circles = np.uint16(np.around(circles))
count = 0
for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    count = count+1

# Print image on screen
cv2.imshow("real_result", img)

# Print how many coins we found
print("Number of coins detected: {}".format(count))

# Check if there is a folder named image_result, if not, than create
if not os.path.exists('image_result'):
    os.makedirs('image_result')

# Saving image in directory
cv2.imwrite('image_result/real_result.jpg', img)

# Press any key to close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
