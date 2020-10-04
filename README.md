## Counting Coins 
### Computer Vision Challenge
### Requirements
```
python 3.6
opencv 4.4.0
numpy 1.19.2
```
#### Counting brazilian real coins
Program developed to detect, highlight and count the number of coins in a determinde image
The program is divided in 5 steps: reading the image, converting to grayscale, applying a blurr filter, applying the HoughCricles function to count, draw the center and border of the coins. 
## Running the program
```
$ python real_counter.py
```
## Results:

1.Reading the desired image. To read the original image was used the funtcion cv2.imread().

![Original Image](https://github.com/EduardoRonchi/CountingCoins/blob/master/real_original.jpg)

2.Convert the image to grayscale. It was used cv2.cvtColor().

![graysale_Image](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_gray.jpg)

3.Apply a Gaussian filter to blur the image. It was used the cv2.GaussianBlur().

![Blurred image](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_blurred.jpg)

4.In the blurred image was applied the HoughCircle function. The output is printed on screen:

![Aplication of HoughCircle](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/real_counter_py.jpg)

5.The function HoughCircle is also responsable for drawing the center and the border of each detected coin. The result is below:

![Result](https://github.com/EduardoRonchi/CountingCoins/blob/master/image_result/real_result.jpg)

#### Counting Dollar Coins
Program developed to detect, highlight and count the number of dollar coins for a given image.
The program was divided into 7 steps: image reading, conversion to grayscale, conversion to binary image, application of morphological filters,
application of the SimpleBlobDetector function, print the number of detected coins and apply the Circle function to draw the outline and the center of each coin.

## Running the program
There are two options for running the dolar_counter.py program, with or without printing all morphological transformations used to achieve the best result.
Run:
```
$ python dolar_counter.py
```
to print on screen only the best morphological transformation or 
```
$ python real_counter.py morph
```
to print on screen all the morphological transformations available.

## Results:

1.Reading the original image.

![Original image](https://github.com/EduardoRonchi/CountingCoins/blob/master/dolar_original.png)

2.Convert to grayscale.

![Grayscale](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_gray_image.png)

3.Applying threshold to transform to binary image. It was used the cv2.threshold() function with threshold equal to 38. 
On this step were needed several attempts to find the best threshold value.
 
![Binary Image](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_mask_image.png)

4.Apply morphological filters. In this stage, several morphological filters were tested and several adjustments to the program were necessary to find the best solution. It was the most challenging step. Several morphological transformations were tested, such as, erosion, dilation, opening, closing, tophat and morphological gradient. The best result was for dilation with a 5x5 kernel and three interactions

![Morphologica_filter](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_dilation.png)

5.Application of the SimpleBlobDetector function. It was necessary to apply several parameters for the correct identification of the coins, parameters such as area, circularity, convexity and inertia.

![SimpleBlobDetector](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_blob_counter.png)

6.The number of coins counted is printed on the terminal, as shown in the image below.

![Coins Detected](https://github.com/EduardoRonchi/CountingCoins/blob/master/assets/dolar_python_py.jpg)

7.Application of the Circle function to draw the centers and contours of the coins. It was needed to save some parameters of the keypoints variable when running the SimpleBlobDetector function, such as x and y coordinates and the diameter of each blob.

![Final result](https://github.com/EduardoRonchi/CountingCoins/blob/master/image_result/dolar_result.png)
