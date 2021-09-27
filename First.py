from os import listdir, getcwd
from os.path import isfile, join
from PIL import Image, ImageEnhance


def get_files_in_directory(directory):
    try:
        return [f for f in listdir(directory) if isfile(join(directory, f))]
    except FileNotFoundError as error:
        print("Error: " + str(error))


def process_image_at_path(imagePath):
    image = Image.open(imagePath)
    imageData = process_image_to_pixel_data(image)
    whitePixels = count_white_pixels_in_list(imageData, 230)

    whiteAsPercentage = whitePixels / len(imageData) * 100
    print(filename)
    print(str(whiteAsPercentage) + "%")


def process_image_to_pixel_data(image):
    contraster = ImageEnhance.Contrast(image)
    alteredImage = contraster.enhance(5.0)
    return list(alteredImage.getdata())


def count_white_pixels_in_list(list, threshold):
    numberOfWhitePixels = 0
    for pixel in list:
        if pixel[0] < threshold or pixel[1] < threshold or pixel[2] < threshold:
            continue
        else:
            numberOfWhitePixels += 1

    return numberOfWhitePixels

currentDir = getcwd()
imageNames = get_files_in_directory(currentDir)

for filename in imageNames:
    fullPath = currentDir + "//" + filename
    try:
        process_image_at_path(fullPath)
    except IOError as error:
        print("Error: Could not open file at path: " + fullPath)


input("Press Enter to Quit...")