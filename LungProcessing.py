import FileAccessLayer as fileLayer
from PIL import Image, ImageEnhance
import ntpath

contrastScalar = 5.0
whiteThreshold = 230.0


# Increase Contrast of an Image
def process_image(image, contrastScalar):
    contraster = ImageEnhance.Contrast(image)
    alteredImage = contraster.enhance(contrastScalar)
    return alteredImage


# Count all the light pixels in an array of pixels. Adjustable threshold
def count_white_pixels_in_list(list, threshold):
    number_of_white_pixels = 0
    for pixel in list:
        if pixel[0] < threshold or pixel[1] < threshold or pixel[2] < threshold:
            continue
        else:
            number_of_white_pixels += 1

    return number_of_white_pixels


def process_folder(folderpath):

    processing_results = []

    for file in fileLayer.all_file_paths_in_directory(folderpath):
        try:  # Attempt something that might fail horribly
            image = Image.open(file)
            alteredImage = process_image(image, contrastScalar)
            pixelData = alteredImage.getdata()
            whitePixels = count_white_pixels_in_list(pixelData, whiteThreshold)
            whiteAsPercentage = whitePixels / len(pixelData) * 100

            processing_results.append(ntpath.basename(file) + "," + str(whiteAsPercentage))

        except IOError as error:  # If the above fails as an IOError, do this
            # Usually do something helpful to prompt the user to fix the issue
            print("Warning: Could not open file at path: " + file)

    return processing_results

