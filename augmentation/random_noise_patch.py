import csv
import os
import random

import cv2
import numpy as np

random.seed(0)


def get_rand_patch(dim_w, dim_h):
    height, width = dim_h, dim_w
    noise_patch_img = np.random.randint(0, 255, (height, width, 3))
    # cv2.imwrite('noise_image.png', noise_image)
    return noise_patch_img


csv_file_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/base_norm_gt.csv'
in_dir_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/Base_and_Aug_Images_PNG'
out_dir_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/test/patch_noise'
counter = 0

with open(csv_file_path, 'r') as csvfile:
    samples = csv.reader(csvfile, delimiter=',')
    for sample in samples:
        print('row count ', counter)
        counter += 1
        img_name = str(sample[0])
        img_path = os.path.join(in_dir_path, img_name)
        img = cv2.imread(img_path)
        copy_img = img.copy()
        no_instances = int(sample[1])
        lstIndex = 2
        list_np_rois = []
        if counter == 1504:
            print('break')
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

        out_img_path = os.path.join(out_dir_path, img_name)
        cv2.imwrite(out_img_path, copy_img)
