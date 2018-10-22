# The code and outputs with Web in the title is only adapted by me, and are not designed by me.
# The source code can be found here:
# https://www.codeproject.com/Articles/8174/Class-to-calculate-HSI-Hue-Saturation-Intensity
# This code and its outputs are used in the report to discuss the flaws in my program, see the report for more on this.

import numpy as np
import cv2

# This code converts RGB to HSI using the method and math discussed on the web page:
# https://www.codeproject.com/Articles/8174/Class-to-calculate-HSI-Hue-Saturation-Intensity Found 17/10 - 2018

# This code is included because it is more efficient than the method from the book, but not as accurate.

# Here the code imports the image that the algorithm will use.
image = cv2.imread("flowers.jpg")
# The dimensions of the image is stored in different variables
height, width,  channels = image.shape

# Three empty arrays are made, for the output images
outputForHValueWeb = np.zeros((height, width, channels), np.uint64)
outputForSValueWeb = np.zeros((height, width, channels), np.uint64)
outputForIValueWeb = np.zeros((height, width, channels), np.uint64)
outputForHSIValueWeb = np.zeros((height, width, channels), np.uint64)

# The data from the imported image is stored in a numpy array
imageData = np.asarray(image)

# This function calculates the Hue in the HSI color space
def calculateHWeb(R, G, B, max, dif, sValue):

    hValue = 0

    # Here the different values of the Hue is calculated based on what color has the highest value in the current pixel.
    # Compared to the method from the book this is more efficient,
    # because it does not require the use of trigonometric functions. It can however be less accurate
    if sValue is not 0:
        if max == R:
            if dif == 0:  # included to avoid division by zero
                dif = 1
            hValue = (60*(G-B)/dif)
        elif max == G:
            hValue = (60*(B-R)/dif+120)
        elif max == B:
            hValue = (60*(R-G)/dif+240)
        if hValue < 0:
            hValue = (60*(B-R)/dif+120)
    else:
        hValue = -1

    return hValue


# This function calculates the Saturation in the HSI color space
def calculateSWeb(iValue, sum, dif):
    if sum == 0:
        sum = 1
    if iValue < 128:
        return 255*(dif/sum)
    else:
        return 255*(dif/(510-sum))


# This function calculates the Intensity in the HSI color space
def calculateIWeb(sum):
    return sum/2


# This is the main function in the programme, this converts the RGB values to HSI
def calculateHSIWeb():
    # This nested for-loop goes through the columns and rows of the imported image
    # The i value goes through the rows and the j value each of the columns in the i rows
    for i in range(len(imageData)):
        for j in range(len(imageData[0])):

            # The color values are imported for each pixel in the loop
            pixel = imageData[i][j]
            B = pixel[0]
            G = pixel[1]
            R = pixel[2]

            # The maximum, minimum, sum and difference values are calculated, from the RGB values at the current pixel
            nImax = max(R, B)
            nImax = max(nImax, G)
            nImin = min(R, B)
            nImin = min(nImin, G)
            nSum = nImin + nImax
            nDifference = nImax - nImin

            # The HSI values are simply set to 0 if the RGB values are not within 0 and 255
            if R < 0 and G < 0 and B < 0 or R > 255 and G > 255 and B > 255:
                hValue = sValue = iValue = 0

                outputForIValueWeb[i, j, 0] = iValue
                outputForIValueWeb[i, j, 1] = iValue
                outputForIValueWeb[i, j, 2] = iValue

                outputForSValueWeb[i, j, 0] = sValue
                outputForSValueWeb[i, j, 1] = sValue
                outputForSValueWeb[i, j, 2] = sValue

                outputForHValueWeb[i, j, 0] = hValue
                outputForHValueWeb[i, j, 1] = hValue
                outputForHValueWeb[i, j, 2] = hValue

                outputForHSIValueWeb[i, j, 0] = hValue
                outputForHSIValueWeb[i, j, 1] = sValue
                outputForHSIValueWeb[i, j, 2] = iValue
            else:

                # Here the Intensity is calculated, simply by calling the previously declared function,
                # with the current pixels RGB values.
                # The calculated values are then put into the output image in grey scale.
                iValue = calculateIWeb(nSum)
                outputForIValueWeb[i, j, 0] = iValue
                outputForIValueWeb[i, j, 1] = iValue
                outputForIValueWeb[i, j, 2] = iValue

                # Here the Saturation is calculated, simply by calling the previously declared function,
                # with the current pixels RGB values.
                # The calculated values are then once again put into the output image in grey scale.
                sValue = calculateSWeb(iValue, nSum, nDifference)
                outputForSValueWeb[i, j, 0] = sValue
                outputForSValueWeb[i, j, 1] = sValue
                outputForSValueWeb[i, j, 2] = sValue

                # Here the Hue is calculated, simply by calling the previously declared function,
                # with the current pixels RGB values.
                # The calculated values are once again put into the output image in grey scale.
                hValue = calculateHWeb(R, G, B, nImax, nDifference, sValue)
                if hValue>255:
                    hValue=255
                elif hValue<0:
                    hValue = 0
                outputForHValueWeb[i, j, 0] = hValue
                outputForHValueWeb[i, j, 1] = hValue
                outputForHValueWeb[i, j, 2] = hValue

                # Here the HSI values are put into the same output image, this has no real purpose,
                # and is mostly just interesting to look at :)
                outputForHSIValueWeb[i, j, 0] = hValue
                outputForHSIValueWeb[i, j, 1] = sValue
                outputForHSIValueWeb[i, j, 2] = iValue


# The main function is called
calculateHSIWeb()

# The the previously blank images are saved to the hard drive and can now be view outside this program
cv2.imwrite('outputHValueWeb.jpg', outputForHValueWeb)
cv2.imwrite('outputSValueWeb.jpg', outputForSValueWeb)
cv2.imwrite('outputIValueWeb.jpg', outputForIValueWeb)
cv2.imwrite('outputHSIValueWeb.jpg', outputForHSIValueWeb)

# Simple debug message
print('The code from the web completed')
