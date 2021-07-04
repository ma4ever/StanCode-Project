"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: This program helps users delete unrelated people or items on images.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_distance = red - pixel.red
    green_distance = green - pixel.green
    blue_distance = blue - pixel.blue
    color_distance = (red_distance ** 2 + green_distance ** 2 + blue_distance ** 2) ** 0.5
    return color_distance


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0
    green_total = 0
    blue_total = 0
    count = 0  # calculate the number of pixel
    for pixel in pixels:
        red_total += pixel.red
        green_total += pixel.green
        blue_total += pixel.blue
        count += 1
    red_average = red_total // count
    green_average = green_total // count
    blue_average = blue_total // count
    return red_average, green_average, blue_average


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages
    """
    red_average, green_average, blue_average = get_average(pixels)

    # set pixels[0] as standard for others to compare
    num = 0  # for number in the list of pixels
    pixel = pixels[num]
    best_pixel_distance = get_pixel_dist(pixel, red_average, green_average, blue_average)
    best_pixel = pixels[0]

    # start comparison
    for pixel in pixels[1:]:
        num += 1
        get_color_distance = get_pixel_dist(pixel, red_average, green_average, blue_average)
        if get_color_distance < best_pixel_distance:
            best_pixel_distance = get_color_distance
            best_pixel = pixels[num]
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)

    # Write code to populate image and create the 'ghost' effect
    # choose the best pixel and print it on the blank image
    for i in range(width):
        for j in range(height):
            result_pixel = result.get_pixel(i, j)
            pixels = []  # place here to avoid indefinitely add items to the pixels
            for image in images:
                pixel = image.get_pixel(i, j)
                pixels.append(pixel)  # add pixels together to make get_best_pixel work
            best_pixel = get_best_pixel(pixels)
            result_pixel.red = best_pixel.red
            result_pixel.green = best_pixel.green
            result_pixel.blue = best_pixel.blue

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
