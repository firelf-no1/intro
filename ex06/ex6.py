##############################################################
# FILE : ex6.py
# WRITER : itai shopen , firelf , 021982038
# EXERCISE : intro2cs ex6 2017-2018
# DESCRIPTION: an image rotators
#############################################################
import ex6_helper
import sys
import math
import copy
NUMBER_OF_ARGUMENTS = 3

ERROR_MESSAGE_ARGUMENTS = "Wrong number of parameters. The correct usage is:" \
                          " ex6.py <image_source> <output > <max_diagonal>"
IMAGE_FILE_LOCATION = 1
IMAGE_OUTPUT_FILE_LOCATION = 2
MAX_DIAGONAL = 3


def check_arg(arg_list):
    """ a progrem that chaecks if the input is ok"""
    if len(arg_list) != NUMBER_OF_ARGUMENTS + 1:
        print(ERROR_MESSAGE_ARGUMENTS)
        return False
    else:
        return True


def num_black(image, th):
    pixel = image
    black_list = []
    white_list = []
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if pixel[i][j] < th:
                black_list.append(pixel[i][j])
            else:
                white_list.append(pixel[i][j])
    return black_list, white_list


def averge_num(list):
    number_list = list
    if sum(number_list) == 0:
        return 0
    else:
        averge = sum(number_list) / len(number_list)
        return averge


def otsu(image):
    # 𝑏𝑙𝑎𝑐𝑘= 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑏𝑙𝑎𝑐𝑘 𝑝𝑖𝑥𝑒𝑙𝑠 (<𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑)
    # 𝑤ℎ𝑖𝑡𝑒= 𝑛𝑢𝑚𝑏𝑒𝑟 𝑜𝑓 𝑤ℎ𝑖𝑡𝑒 𝑝𝑖𝑥𝑒𝑙𝑠 (≥𝑡ℎ𝑟𝑒𝑠ℎ𝑜𝑙𝑑)
    # 𝑚𝑒𝑎𝑛_𝑏𝑙𝑎𝑐𝑘 = 𝑎𝑣𝑒𝑟𝑎𝑔𝑒 𝑣𝑎𝑙𝑢𝑒 𝑜𝑓 𝑏𝑙𝑎𝑐𝑘 𝑝𝑖𝑥𝑒𝑙𝑠
    # 𝑚𝑒𝑎𝑛_𝑤ℎ𝑖𝑡𝑒 = 𝑎𝑣𝑒𝑟𝑎𝑔𝑒 𝑣𝑎𝑙𝑢𝑒 𝑜𝑓 𝑤ℎ𝑖𝑡𝑒 𝑝𝑖𝑥𝑒𝑙𝑠
    intra_variance = [0 for x in range(0, 256)]
    for th in range(0, 256):
        black_list, white_list = num_black(image, th)
        black = len(black_list)
        white = len(white_list)
        mean_black = averge_num(black_list)
        mean_white = averge_num(white_list)
        intra_variance[th] = black * white * (mean_black - mean_white) ** 2
    max_th_valve = intra_variance.index(max(intra_variance))
    return max_th_valve


def threshold_filter(image):
    pixel = image
    threshold = otsu(image)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if pixel[i][j] < threshold:
                pixel[i][j] = 0
            else:
                pixel[i][j] = 255
    return pixel


def x_check(x):
    p = abs(x)
    if p > 255:
        p = 255
    return p


def apply_filter(image, filter):
    pixel = image
    new_image = image
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if i == 0:
                if j == 0:
                    x = (filter[0][0] * pixel[i][j] + filter[0][1] *
                         pixel[i][j] + filter[0][2] * pixel[i][j] +
                         filter[1][0] * pixel[i][j] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i][j] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i + 1][j + 1])
                    new_image[i][j] = int(x_check(x))
                elif j == len(image[i]) - 1:
                    x = (filter[0][0] * pixel[i][j] + filter[0][1] *
                         pixel[i][j] + filter[0][2] * pixel[i][j] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j] +
                         filter[2][0] * pixel[i + 1][j - 1] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i][j])
                    new_image[i][j] = int(x_check(x))
                else:
                    x = (filter[0][0] * pixel[i][j] + filter[0][1] *
                         pixel[i][j] + filter[0][2] * pixel[i][j] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i + 1][j - 1] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i + 1][j + 1])
                    new_image[i][j] = int(x_check(x))
            elif i == len(image) - 1:
                if j == 0:
                    x = (filter[0][0] * pixel[i][j] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i - 1][j + 1] +
                         filter[1][0] * pixel[i][j] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i][j] + filter[2][1] *
                         pixel[i][j] + filter[2][2] * pixel[i][j])
                    new_image[i][j] = int(x_check(x))
                elif j == len(image[i]) - 1:
                    x = (filter[0][0] * pixel[i - 1][j - 1] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i][j] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j] +
                         filter[2][0] * pixel[i][j] + filter[2][1] *
                         pixel[i][j] + filter[2][2] * pixel[i][j])
                    new_image[i][j] = int(x_check(x))
                else:
                    x = (filter[0][0] * pixel[i - 1][j - 1] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i - 1][j + 1] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i][j] + filter[2][1] *
                         pixel[i][j] + filter[2][2] * pixel[i][j])
                    new_image[i][j] = int(x_check(x))
            else:
                if j == 0:
                    x = (filter[0][0] * pixel[i][j] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i - 1][j + 1] +
                         filter[1][0] * pixel[i][j] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i][j] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i + 1][j + 1])
                    new_image[i][j] = int(x_check(x))
                elif j == len(image[i]) - 1:
                    x = (filter[0][0] * pixel[i - 1][j - 1] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i][j] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j] +
                         filter[2][0] * pixel[i + 1][j - 1] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i][j])
                    new_image[i][j] = int(x_check(x))
                else:
                    x = (filter[0][0] * pixel[i - 1][j - 1] + filter[0][1] *
                         pixel[i - 1][j] + filter[0][2] * pixel[i - 1][j + 1] +
                         filter[1][0] * pixel[i][j - 1] + filter[1][1] *
                         pixel[i][j] + filter[1][2] * pixel[i][j + 1] +
                         filter[2][0] * pixel[i + 1][j - 1] + filter[2][1] *
                         pixel[i + 1][j] + filter[2][2] * pixel[i + 1][j + 1])
                    new_image[i][j] = int(x_check(x))
    return new_image


def detect_edges(image):
    new_image = apply_filter(image, [[-1 / 8, -1 / 8, -1 / 8],
                                     [-1 / 8, 1, -1 / 8],
                                     [-1 / 8, -1 / 8, -1 / 8]])
    return new_image


def downsample_by_3(image):
    pixel = image
    new_image = list()
    for i in range(1, len(image), 3):
        row_list = list()
        for j in range(1, len(image[i]), 3):
            x = ((pixel[i - 1][j - 1] + pixel[i - 1][j] +
                 pixel[i - 1][j + 1] +
                 pixel[i][j - 1] + pixel[i][j] + pixel[i][j + 1] +
                 pixel[i + 1][j - 1] + pixel[i + 1][j] +
                 pixel[i + 1][j + 1]) / 9)
            row_list.append(int(x))
        new_image.append(row_list)
    return new_image


def image_diagonal(image):
    image_dia = (((len(image) ** 2) + (len(image[0]) ** 2)) ** 0.5)
    return image_dia


def downsample(image, max_diagonal_size):
    pixel = image
    image_dia = image_diagonal(pixel)
    while image_dia > max_diagonal_size:
        pixel = downsample_by_3(pixel)
        image_dia = image_diagonal(pixel)
    return pixel


def pixel_distance(r1, c1, r2, c2):
    distance = ((((r1 - r2) ** 2) + ((c1 - c2) ** 2)) ** 0.5)
    distance1 = x_check(distance)
    if distance1 > 2:
        return False
    else:
        return True


def line_pixel_counter(line, image):
    line_counter = 0
    lines_total_rank = 0
    row_wh_index = {"row": 0, "column": 0}
    for x in range(0, len(line)):
        if image[line[x][0]][line[x][1]] == 255:
            if pixel_distance(row_wh_index["row"], row_wh_index["column"],
                              line[x][0], line[x][1]) == True:
                line_counter += 1
                row_wh_index["row"] = line[x][0]
                row_wh_index["column"] = line[x][1]
            else:
                lines_total_rank += (line_counter ** 2)
                line_counter = 0
                row_wh_index["row"] = line[x][0]
                row_wh_index["column"] = line[x][1]
    return lines_total_rank


def get_angle(image):
    pixel = threshold_filter(image)
    angle_list = [0 for a in range(0, 180)]
    diagonal = int(image_diagonal(pixel))
    for t in range(0, diagonal + 1):
        for a in range(0, len(angle_list)):
            if 0 < a < 90:
                line_top = ex6_helper.pixels_on_line(pixel, math.radians(a),
                                                     t, True)
                angle_list[a] += line_pixel_counter(line_top, pixel)
                line_bottom = ex6_helper.pixels_on_line(pixel, math.radians(a),
                                                        t, False)
                angle_list[a] += line_pixel_counter(line_bottom, pixel)
            else:
                line = ex6_helper.pixels_on_line(pixel, math.radians(a), t)
                angle_list[a] += line_pixel_counter(line, pixel)
    largest_line = angle_list.index(max(angle_list))
    return largest_line


def find_center(image):
    y = len(image) / 2
    x = len(image[0]) / 2
    return int(y), int(x)


def new_location(r, c, angle):
    x = int((r * math.cos(angle)) - (c * math.sin(angle)))
    y = int((r * math.sin(angle)) + (c * math.cos(angle)))
    return x, y


def rotate(image, angle):
    pixel = image
    alfa_angle = math.radians((-angle))
    r_angle = math.radians(angle)
    w = len(pixel)
    h = len(pixel[0])
    nw = abs(int((h * math.sin(r_angle)) + (w * math.cos(r_angle))))
    nh = abs(int((h * math.cos(r_angle)) + (w * math.sin(r_angle))))
    y, x = find_center(image)
    new_list = [[0] * nw for _ in range(0, nh)]
    ny, nx = find_center(new_list)
    for i in range(0, len(new_list)):
        for j in range(0, len(new_list[i])):
            r, c = new_location(i - ny, j - nx, alfa_angle)
            if r + x >= h or r + x <= 0:
                new_list[i][j] = 0
            elif c + y >= w or c + y <= 0:
                new_list[i][j] = 0
            else:
                new_list[i][j] = image[r + x][c + y]
    return new_list


def make_correction(image, max_diagonal):
    pixel = copy.deepcopy(image)
    small_image = downsample(pixel, max_diagonal)
    bw_image = threshold_filter(small_image)
    edges_image = detect_edges(bw_image)
    bw2_image = threshold_filter(edges_image)
    angle = get_angle(bw2_image)
    rotated_image = rotate(image, 180 - angle)
    return rotated_image


def main(argv):
    if check_arg(argv) == False:
        return
    image = sys.argv[1]
    output_file_name = sys.argv[2]
    max_diagonal = sys.argv[3]
    # new_image = make_correction(image, max_diagonal)
    pixel = copy.deepcopy(image)
    small_image = downsample(pixel, max_diagonal)
    bw_image = threshold_filter(small_image)
    edges_image = detect_edges(bw_image)
    bw2_image = threshold_filter(edges_image)
    angle = get_angle(bw2_image)
    rotated_image = rotate(image, 180 - angle)
    ex6_helper.save(rotated_image, output_file_name)


if __name__ == "__main__":
    main(sys.argv)
