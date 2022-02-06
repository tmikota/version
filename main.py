# This is a sample Python script.
import random
import re
# Press Alt+Shift+X to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def remove_elements(input_list, n):
    """
    removes n random items from a list
    :param input_list:
    :param n: how many random items to remove
    :return:
    """
    to_delete = set(random.sample(range(len(input_list)), n))
    return [x for i, x in enumerate(input_list) if not i in to_delete]


def generate_sequence(sframe, eframe, remove_frames=0, padding=4):
    """
    creates a sequence from sframe to eframe
    :param basedir: location to create the frames
    :param remove_frames: if set, remove this number of frames.

    :return:
    """
    current_frame = sframe
    sequence = []
    while current_frame <= eframe:
        frame_string = format(current_frame, get_padding_string(padding))
        filestring = "test_file.{}.txt".format(frame_string)
        sequence.append(filestring)
        current_frame += 1
    if remove_frames:
        sequence = remove_elements(sequence, remove_frames)

    return sequence


def get_frame_numbers(file_list):
    numbers = []
    regex = re.compile(r'[\d]{3,}')
    for s in file_list:
        frame_num = re.search(regex, s)
        if frame_num:
            padding = len(frame_num.group())
            numbers.append(int(frame_num.group()))
    return sorted(numbers), padding


def get_file_numbers(number_list, padding):
    """
    formats a list of numbers as a sequence:
    1-1000
    1-10, 14-33, 44, 66-100
    :param number_list:
    :return:
    """
    padding_string = get_padding_string(padding)
    sframe = number_list[0]
    eframe = number_list[-1]
    missing = find_missing(number_list, padding)
    if missing:
        print(missing)
    else:
        return "{}-{}".format(format(sframe, padding_string), format(eframe, padding_string))


def get_padding_string(padding):
    if padding < 9:
        padding_string = "0{}".format(padding)
    else:
        padding_string = str(padding)
    return padding_string


def find_missing(sequence, padding):
    """
    finds missing numbers in a number sequence

    :param sequence:
    :return:
    """
    padding_string = get_padding_string(padding)
    sframe = sequence[0]
    eframe = sequence[-1]
    missing = sorted(set(range(sframe, eframe)) - set(sequence))
    bframe = None
    sequence_string = ''
    for m in missing:
        if not bframe:
            bframe = sframe
            bstring = format(bframe, padding_string)
        frange = "{}-{}".format(bstring, format(m-1, padding_string))
        if not sequence_string:
            sequence_string = frange
        else:
            sequence_string = "{}, {}".format(sequence_string, frange)
        bframe = m+1
    if bframe:
        end_range = "{}-{}".format(format(bframe, padding_string), format(eframe, padding_string))
    else:
        return "{}-{}".format(format(sframe, padding_string), format(eframe, padding_string))
    if end_range:
        return "{}, {}".format(sequence_string, end_range)


def get_frame_range(file_list):
    frame_numbers, pad = get_frame_numbers(file_list)
    nums = get_file_numbers(frame_numbers, padding=pad)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_list = generate_sequence(sframe=1, eframe=100, remove_frames=4, padding=3)
    get_frame_range(file_list)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
