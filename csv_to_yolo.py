import csv
import os
from shutil import copyfile

import cv2

import bunch_2_yolo
import image_utils
from Bunch import Bunch
from image_utils import get_file_number

''' e.g the file should be in this format "000015.png,3,640.0,131.0,712.0,211.0,15,640.0,212.0,710.0,253.0,17,640.0,254.0,709.0,293.0,17"
'''


def convert_csv_to_yolo_format(in_dir, out_dir, gt_csv_file_path):
    '''This Fn takes the input csv file and write the images and texts file as in yolo format.'''
    counter = 0
    total_roi_instances = 0

    with open(gt_csv_file_path, 'r') as csvfile:
        samples = csv.reader(csvfile, delimiter=',')
        for sample in samples:
            print('row count ', counter)
            counter += 1
            img_name = str(sample[0])
            img_path = os.path.join(in_dir, img_name)
            img_no = get_file_number(img_name)
            img = cv2.imread(img_path)
            no_instances = int(sample[1])
            total_roi_instances += no_instances
            lstIndex = 2
            list_instances = []
            for ii in range(no_instances):
                x_min = float(sample[lstIndex])
                lstIndex += 1
                y_min = float(sample[lstIndex])
                lstIndex += 1
                x_max = float(sample[lstIndex])
                lstIndex += 1
                y_max = float(sample[lstIndex])
                lstIndex += 1
                # class_lbl = list_class_name.index(class_name)
                class_lbl = int(sample[lstIndex])
                lstIndex += 1
                instance = Bunch(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, lbl=class_lbl)
                list_instances.append(instance)

            llist_yolo = bunch_2_yolo.get_yolo_llist(list_instances, img)
            txt_path, txt_name = image_utils.get_txt_path_name_frm_index(int(img_no), out_dir)
            old_img_path = os.path.join(in_dir, img_name)
            new_img_path, new_img_name = image_utils.get_img_path_name_frm_index(int(img_no), out_dir)
            copyfile(old_img_path, new_img_path)
            f = open(txt_path, 'w')
            writer = csv.writer(f, delimiter=' ')
            for list_yolo in llist_yolo:
                writer.writerow(list_yolo)
            f.close()

    print('total roi instances = ', total_roi_instances)
