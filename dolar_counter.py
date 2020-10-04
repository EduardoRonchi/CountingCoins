# Program to count dollar coins
import numpy as np
import cv2
import os
import sys


# Function used to detect blobs. Returns the image with drawing on blobs
# and the coordinates and diameter of the blobs
def blob_detector(image):
    # Set our filtering parameters
    # Initialize parameter settings using cv2.SimpleBlobDetector
    params = cv2.SimpleBlobDetector_Params()

    # Set Area filtering parameters
    params.filterByArea = True
    params.maxArea = 100000

    # Set Circularity filtering parameters
    params.filterByCircularity = True
    params.minCircularity = 0.58

    # Set Convexity filtering parameters
    params.filterByConvexity = True
    params.minConvexity = 0.01
    params.maxConvexity = 0.99

    # Set inertia filtering parameters
    params.filterByInertia = True
    params.minInertiaRatio = 0.01

    # Create a detector with the parameters
    detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs
    keypoints = detector.detect(image)

    # Get the coordinates and diameter of each blob
    x_coordinate = []
    y_coordinate = []
    s_diameter = []
    for keyPoint in keypoints:
        x_coordinate.append(keyPoint.pt[0])
        y_coordinate.append(keyPoint.pt[1])
        s_diameter.append(keyPoint.size)

    # Draw blobs on image as red circles
    blank = np.zeros((1, 1))
    blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255),
                              cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    number_of_blobs = len(keypoints)

    # Print the number of coins detected
    print("Number of coins detected: {}".format(number_of_blobs))

    return blobs, x_coordinate, y_coordinate, s_diameter


# Applying several morphological transformations
# to choose the best for the application
def morphological_transformations(image):

    kernel = np.ones((5, 5), np.uint8)
    dilation_ = cv2.dilate(image, kernel, iterations=3)
    erosion_ = cv2.erode(image, kernel, iterations=1)
    opening_ = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
    closing_ = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    mg_ = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
    th_ = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

    return dilation_, erosion_, opening_, closing_, mg_, th_


def main():
    # Choose 'print_all_filters = 1' to print all morphological filters used to achieve the best result
    # Choose any other value to print only the best result
    if len(sys.argv) > 1:
        print_all_filters = sys.argv[1]
    else:
        print_all_filters = 0

    # Load an color image with opencv
    img = cv2.imread('dolar_original.png')

    # Print the loaded image
    cv2.imshow("Original Image", img)

    # Convert image to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Print the gray image
    cv2.imshow("Gray Image", gray)

    # Transform the gray image to binary
    _, mask = cv2.threshold(gray, 38, 255, cv2.THRESH_BINARY_INV)

    # Print the Binary image
    cv2.imshow("Binary Image", mask)

    # Calls function that returns 6 different morphological transformations
    # Passing mask image as input for the function
    dilation, erosion, opening, closing, mg, th = morphological_transformations(mask)

    # Titles and images to be printed
    titles = ['gray', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'morphgradient', 'tophat']
    images = [gray, mask, dilation, erosion, opening, closing, mg, th]

    # Printing images with morphological transformations
    if print_all_filters == 'morph':

        for i in range(len(titles)):
            cv2.imshow("{}".format(titles[i]), images[i])

    else:
        cv2.imshow("Morphological transform: dilation", dilation)

    # Call blob_detector function with image dilation as input and
    # number of blobs, coordinates and size (diameter) of blobs as output
    blob_counter, x, y, s = blob_detector(dilation)

    # Converting the float valuer received to int (circle function only accepts integers)
    x = [int(x) for x in x]
    y = [int(y) for y in y]

    # Drawing the circles in the original image
    for i in range(len(x)):
        # Draw the contour
        # s is divided by 2 because the function accepts radius and s is in diameter
        cv2.circle(img, (x[i], y[i]), int(s[i]/2), (0, 255, 0), 3)

        # Draw the center
        cv2.circle(img, (x[i], y[i]), 5, (255, 0, 0), -1)

    # Check if there is a folder named image_result, if not, than create
    if not os.path.exists('image_result'):
        os.makedirs('image_result')

    # Saving image in directory
    cv2.imwrite('image_result/dolar_result.png', img)

    # Print desired images
    cv2.imshow("Blobs Found", blob_counter)
    cv2.imshow("Final_result", img)

    # Press any key to close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


if __name__ == '__main__':
    main()
