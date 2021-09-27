# int = 1, 2, -20 // number of users logged in
# floats = 1, 1.1, -342.6543678 // Percentage of users who have paid
# double = like floats but twice the accuracy / size
# strings = "", "a", "Full sentences!@$#@^%#&^%*&^)(][;'" // Username, passwords, urls,
# bool (Boolean) = True or False
# comments in python, use #

import time
from os import listdir, getcwd
from os.path import isfile, join
from PIL import Image, ImageEnhance

contrastScalar = 5.0
whiteThreshold = 230.0


# Return all files for a given directory
def allFilePaths(directory):
    allFilePaths = []

    for file in listdir(directory):
        fullFilePath = join(directory, file)
        if isfile(fullFilePath):
            allFilePaths.append(fullFilePath)

    return allFilePaths


# Increase Contast of an Image
def process_image(image):
    contraster = ImageEnhance.Contrast(image)
    alteredImage = contraster.enhance(contrastScalar)
    return alteredImage


# Count all the light pixels in an array of pixels. Adjustible threshold
def count_white_pixels_in_list(list, threshold):
    numberOfWhitePixels = 0
    for pixel in list:
        if pixel[0] < threshold or pixel[1] < threshold or pixel[2] < threshold:
            continue
        else:
            numberOfWhitePixels += 1

    return numberOfWhitePixels


def outputToFile(fileName, whitePercent, asCSV):
    outputFile = open("demofile.txt", "a")

    if asCSV:
        outputFile.write(fileName + "," + str(whitePercent) + "\n")
    else:
        outputFile.write(fileName + "\n")
        outputFile.write(str(whitePercent) + "% air in slide\n")
        outputFile.write("------\n\n")

    outputFile.close()


print("All File Paths")

for file in allFilePaths(getcwd()):
    try:  # Attempt something that might fail horribly
        image = Image.open(file)
        alteredImage = process_image(image)
        pixelData = alteredImage.getdata()
        whitePixels = count_white_pixels_in_list(pixelData, whiteThreshold)
        whiteAsPercentage = whitePixels / len(pixelData) * 100

        outputToFile(file, whiteAsPercentage, False)

    except IOError as error:  # If the above fails as an IOError, do this
        print(
            "Error: Could not open file at path: " + file)  # Usually do something helpful to prompt the user to fix the issue

print("Done, sleeping for 5")
time.sleep(5)