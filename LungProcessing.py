from os import listdir
from os.path import isfile, join
from PIL import Image, ImageEnhance
import ntpath

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
def process_image(image, contrastScalar):
    contraster = ImageEnhance.Contrast(image)
    alteredImage = contraster.enhance(contrastScalar)
    return alteredImage


# Count all the light pixels in an array of pixels. Adjustable threshold
def count_white_pixels_in_list(list, threshold):
    numberOfWhitePixels = 0
    for pixel in list:
        if pixel[0] < threshold or pixel[1] < threshold or pixel[2] < threshold:
            continue
        else:
            numberOfWhitePixels += 1

    return numberOfWhitePixels


def process_folder(folderPath, outputFileName):

    outputFile = open(outputFileName, "a")
    outputFile.write("Image Name,Air Percentage\n")

    for file in allFilePaths(folderPath):
        try:  # Attempt something that might fail horribly
            image = Image.open(file)
            alteredImage = process_image(image, contrastScalar)
            pixelData = alteredImage.getdata()
            whitePixels = count_white_pixels_in_list(pixelData, whiteThreshold)
            whiteAsPercentage = whitePixels / len(pixelData) * 100

            outputFile.write(ntpath.basename(file) + "," + str(whiteAsPercentage) + "\n")

        except IOError as error:  # If the above fails as an IOError, do this
            # Usually do something helpful to prompt the user to fix the issue
            print("Warning: Could not open file at path: " + file)

    outputFile.close()
