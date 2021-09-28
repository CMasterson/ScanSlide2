import os
from os import listdir
from os.path import isfile, join


# Return all files for a given directory
def all_file_paths_in_directory(directory):
    paths = []

    for file in listdir(directory):
        fullpath = join(directory, file)
        if isfile(fullpath):
            paths.append(fullpath)

    return paths


def write_results_to_file(results, filename):
    output_file = open(filename, "a")
    output_file.write("Image Name,Air Percentage\n")
    for result in results:
        output_file.write(result + "\n")

    output_file.close()


def file_exists(filename):
    return os.path.isfile(filename)


def open_file(filename):
    os.startfile(filename)
