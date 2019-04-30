import os
from PIL import Image
import math


def load_image(image_filename):
    """  load an image from an image file and return it as a list of lists """

    img = Image.open(image_filename)
    gray_img = img.convert("L")
    image = lists_from_pil_image(gray_img)
    return image


def save(image, filename):
    """ save an image (as list of lists) to a file """
    mosaic = pil_image_from_lists(image)
    output_dir = os.path.dirname(filename)

    if output_dir != "" and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    mosaic.save(filename)


def show(image):
    """ display an image (as list of lists) """
    mosaic = pil_image_from_lists(image)
    mosaic.show()


def get_diagonal_angle(image):
    """returns the angle of the diagonal of an image"""
    height = len(image)
    if height > 0:
        row_lengths = [len(row) for row in image]
        width = min(row_lengths)
        if width != max(row_lengths):
            print("Error: Image rows are not consistent!")
    else:
        print("Error: Empty Image!")
    return 180*math.atan(height/width)/math.pi


def pixels_on_line(image, angle, distance, top=True):
    """returns a list of of following pixels in an image that are on the line
    of specific angle (in radians) and distance from top left pixel.
    """
    if distance < 0:
        return
    angle = angle % math.pi
    image_size = get_image_size(image)
    image_height, image_width = image_size
    if angle == 0:
        column = 0
        row = int(distance)
    elif angle < math.pi / 2:
        if top:
            row = int(distance / math.cos(angle))
            column = 0
        else:
            row = 0
            column = int(distance / math.sin(angle))
    elif angle == math.pi / 2:
        column = int(distance)
        row = 0
    else:
        row = int(distance / math.sin(angle - math.pi/2))
        if row < image_height:
            column = 0
        else:
            temp_row = row - image_height
            column = int(temp_row / math.tan(math.pi - angle) )
            row = image_height - 1

    return pixels_on_line_from_origin(image, angle, (row, column))























def pil_image_from_lists(image_as_lists):
    """ Generate an Image obj from list of lists """
    height = len(image_as_lists)
    width = min([len(image_as_lists[i]) for i in range(height)])
    im = Image.new("L", (width, height))
    for i in range(width):
        for j in range(height):
            im.putpixel((i, j), image_as_lists[j][i])
    return im


def lists_from_pil_image(image):
    """ Turn an Image obj to a list of lists """
    width, height = image.size
    pixels = list(image.getdata())
    pixels = [pixels[i * width:(i + 1) * width] for i in range(height)]
    return pixels

def get_image_size(image):
    height = len(image)
    if height > 0:
        row_lengths = [len(row) for row in image]
        width = min(row_lengths)
        if width == max(row_lengths):
            return (height, width)
        print("Error: Image rows are not consistent!")
    print("Error: Empty Image!")

def within_borders(pixel_location, image_size):
        in_borders = True
        for i in range(2):
            if pixel_location[i] < 0 or pixel_location[i] >= image_size[i]:
                in_borders = False
        return in_borders

def pixels_on_line_from_origin(image, angle, first_pixel):
    """
    assumptions:
    0 <= angle < pi
    distance >= 0
    """
    image_size = get_image_size(image)
    image_height, image_width = image_size
    pixels = []
    ratio = math.tan(angle)
    if not within_borders(first_pixel, image_size):
        pass
    elif angle == 0:
        row = first_pixel[0]
        for column in range(first_pixel[1], image_width):
            pixels.append([row, column])
    elif angle < math.pi/2:
        row = first_pixel[0]
        for column in range(first_pixel[1], image_width):
            unrounded = first_pixel[0] + (column+1-first_pixel[1])*ratio
            curr_pixel = [row, column]
            while unrounded > row and within_borders(curr_pixel, image_size):
                pixels.append(curr_pixel)
                if unrounded >= row + 1:
                    row += 1
                    curr_pixel = [row, column]
                else:
                    break

            if not within_borders(curr_pixel, image_size):
                break

    elif angle == math.pi/2:
        column = first_pixel[1]
        for row in range(first_pixel[0], image_height):
            pixels.append([row, column])
    #pi < angle < 2pi
    else:
        row = first_pixel[0]
        for column in range(first_pixel[1], image_width):
            unrounded = first_pixel[0] + (column + 1 - first_pixel[1]) * ratio
            curr_pixel = [row, column]
            while unrounded < row and within_borders(curr_pixel, image_size):
                pixels.append(curr_pixel)
                if unrounded <= row - 1:
                    row -= 1
                    curr_pixel = [row, column]
                else:
                    break

            if not within_borders(curr_pixel, image_size):
                break

    return pixels





