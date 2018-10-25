import csv
import os
import random

import cv2
import numpy as np

from augmentation.brightness_aug import csv_reader
from image_utils import get_img_path_name_frm_index

random.seed(0)


def get_rand_patch(dim_w, dim_h):
    height, width = dim_h, dim_w
    noise_patch_img = np.random.randint(0, 255, (height, width, 3))
    # cv2.imwrite('noise_image.png', noise_image)
    return noise_patch_img


# csv_file_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/base_norm_gt.csv'
# in_dir_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/Base_and_Aug_Images_PNG'
# out_dir_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/test/patch_noise'


def generate_nois_patch_images_and_GT(in_dir, out_dir, csv_path):
    counter = 0
    csv_file_path = os.path.join(out_dir, 'groundTruth.csv')
    grount_truth_csv = open(csv_file_path, 'w')
    writer = csv.writer(grount_truth_csv, delimiter=',')
    samples = csv_reader(csv_path)
    random.shuffle(samples)
    for sample in samples:
        print('row count ', counter)
        if counter == 5000:
            break
            print('break')
        img_name = str(sample[0])
        img_path = os.path.join(in_dir, img_name)
        img = cv2.imread(img_path)
        copy_img = img.copy()
        no_instances = int(sample[1])
        lstIndex = 2

        for ii in range(no_instances):
            x1 = float(sample[lstIndex])
            lstIndex += 1
            y1 = float(sample[lstIndex])
            lstIndex += 1
            x2 = float(sample[lstIndex])
            lstIndex += 1
            y2 = float(sample[lstIndex])
            lstIndex += 1
            class_lbl = float(sample[lstIndex])
            lstIndex += 1
            roi_width = x2 - x1
            roi_height = y2 - y1
            if roi_width > 10 and roi_height > 5:
                per_dim_w = int(0.25 * roi_width)
                per_dim_h = int(0.25 * roi_height)
                noise_img = get_rand_patch(per_dim_w, per_dim_h)
                paste_x = random.randint(x1, x2 - per_dim_w - 1)
                paste_y = random.randint(y1, y2 - per_dim_h - 1)
                if (paste_x + per_dim_w) > 720:
                    shift_x = (paste_x + per_dim_w) - 720
                    paste_x = paste_x - shift_x - 1
                copy_img[paste_y:paste_y + per_dim_h, paste_x:paste_x + per_dim_w] = noise_img

        out_img_path, out_img_name = get_img_path_name_frm_index(counter, out_dir)
        cv2.imwrite(out_img_path, copy_img)
        sample[0] = out_img_name
        writer.writerow(sample)
        counter += 1
        # test
        # draw_rectangle(sample, out_img_path)
    grount_truth_csv.close()
