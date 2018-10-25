import csv
import os
import random

import cv2
import numpy as np

from image_utils import get_img_path_name_frm_index
from merge2 import extract_coordinates_from_csv_row


def get_bright_image(img, aug_index):
    if aug_index == True:
        aug_value = random.randint(40, 45)
        arr = np.zeros((1, 1, 3)) + aug_value
        bright_img = np.minimum(img + arr, 255)
    else:
        aug_value = random.randint(30, 35) * -1
        arr = np.zeros((1, 1, 3)) + aug_value
        bright_img = np.maximum(img + arr, 0)

    return bright_img


def get_out_img_name(in_img_path):
    img_dir, img_name = os.path.split(in_img_path)
    img_no = int(os.path.splitext(img_name)[0])
    img_name = "%6.6d.png" % (img_no + aug_img_count)
    return img_name


def runner(in_dir, out_dir, csv_path):
    aug_flag = True
    counter = 0
    csv_file_path = os.path.join(out_dir, 'groundTruth.csv')
    grount_truth_csv = open(csv_file_path, 'w')
    writer = csv.writer(grount_truth_csv, delimiter=',')
    list_images_path = csv_reader(csv_path)
    random.shuffle(list_images_path)
    for item in list_images_path:
        if counter == 5000:
            break
        img_path = os.path.join(in_dir, item[0])
        img = cv2.imread(img_path)
        bright_img = get_bright_image(img, aug_flag)
        out_img_path, out_img_name = get_img_path_name_frm_index(counter, out_dir)
        cv2.imwrite(out_img_path, bright_img)
        aug_flag = not aug_flag
        item[0] = out_img_name
        writer.writerow(item)
        print('counter = ', counter)
        counter += 1
        # test
        #  draw_rectangle(item, out_img_path)
    grount_truth_csv.close()


def csv_reader(csv_path):
    with open(csv_path, 'r') as src_csv_file:
        csv_data = csv.reader(src_csv_file, delimiter=',')
        csv_rows = []
        for csv_row in csv_data:
            csv_rows.append(extract_coordinates_from_csv_row(csv_row))
        return csv_rows
