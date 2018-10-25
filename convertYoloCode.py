import csv
import os

import cv2

list_class_name = ['B31', 'A33', 'C02', 'B32', 'E03', 'C44', 'A04', 'C79', 'A03',
                   'C11', 'A05', 'C80', 'B46', 'D10', 'C86', 'B28', 'B02', 'E08', 'C08', 'B39']

in_dir = '/home/vaneesh/Drive/ML/VishalSharedFIles/9May/FinalTask/Combine/orginal/images'
out_dir = '/home/vaneesh/Drive/ML/VishalSharedFIles/9May/FinalTask/Combine/yoloConverted'

gt_csv_file_path = '/home/vaneesh/Drive/ML/VishalSharedFIles/9May/FinalTask/Combine/orginal/augmentGTAll.csv'


class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)


def get_width_height_img(img):
    height, width, channels = img.shape
    return width, height


def get_txt_path(img_index):
    txt_name = "%6.6d.txt" % (img_index)
    txt_path = os.path.join(out_dir, txt_name)
    return txt_path, txt_name


def get_yolo_llist(list_instance, img):
    llist_yolo = []
    img_w, img_h = get_width_height_img(img)
    inv_imgw = 1 / img_w
    inv_imgh = 1 / img_h

    for instance in list_instance:
        x_min, y_min, x_max, y_max, lbl = instance.x_min, instance.y_min, instance.x_max, instance.y_max, instance.lbl
        x_yolo = ((x_min + x_max) / 2) * inv_imgw
        y_yolo = ((y_min + y_max) / 2) * inv_imgh
        w_yolo = (x_max - x_min) * inv_imgw
        h_yolo = (y_max - y_min) * inv_imgh
        tmp_list = [lbl, x_yolo, y_yolo, w_yolo, h_yolo]
        llist_yolo.append(tmp_list)

    return llist_yolo


counter = 0
total_roi_instances = 0
with open(gt_csv_file_path, 'r') as csvfile:
    samples = csv.reader(csvfile, delimiter=',')
    for sample in samples:
        print('row count ', counter)
        counter += 1
        img_dir, img_name = os.path.split(str(sample[0]))
        img_no, img_ext = os.path.splitext(img_name)
        img_path = os.path.join(in_dir, img_name)
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
            # class_name = (sample[lstIndex])
            # class_lbl = list_class_name.index(class_name)
            class_lbl = int(sample[lstIndex])
            lstIndex += 1
            instance = Bunch(x_min=x_min, y_min=y_min, x_max=x_max, y_max=y_max, lbl=class_lbl)
            list_instances.append(instance)

        llist_yolo = get_yolo_llist(list_instances, img)
        txt_path, txt_name = get_txt_path(int(img_no))
        f = open(txt_path, 'w')
        writer = csv.writer(f, delimiter=' ')
        for list_yolo in llist_yolo:
            writer.writerow(list_yolo)
        f.close()

print('total roi instances = ', total_roi_instances)
