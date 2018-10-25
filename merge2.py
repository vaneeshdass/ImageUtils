import csv
import os
from shutil import copyfile

from image_utils import get_img_path_name_frm_index


def merge_dirs_csvs(path_objs, out_dir):
    # dict ={}
    img_counter = 0
    csv_file = os.path.join(out_dir, 'groundTruth.csv')
    merged_csv_file = open(csv_file, 'w')
    writer = csv.writer(merged_csv_file, delimiter=',')
    for item in path_objs:
        with open(item.csv_path, 'r') as src_csv_file:
            csv_data = csv.reader(src_csv_file, delimiter=',')
            for csv_row in csv_data:
                coordinates_list = extract_coordinates_from_csv_row(csv_row)
                old_img_path = os.path.join(item.dir_path, coordinates_list[0])
                new_img_path, new_img_name = get_img_path_name_frm_index(img_counter, out_dir)
                copyfile(old_img_path, new_img_path)
                coordinates_list[0] = new_img_name
                writer.writerow(coordinates_list)
                print('writing - ', img_counter)
                img_counter += 1

    merged_csv_file.close()


def extract_coordinates_from_csv_row(row):
    counter = 2
    img_name = str(row[0])
    no_of_instances = int(row[1])
    coordinates_list = [img_name, no_of_instances]
    for ii in range(no_of_instances):
        x_min = float(row[counter])
        counter += 1
        y_min = float(row[counter])
        counter += 1
        x_max = float(row[counter])
        counter += 1
        y_max = float(row[counter])
        counter += 1
        class_lbl = int(row[counter])
        counter += 1
        coordinates_list.extend([x_min, y_min, x_max, y_max, class_lbl])
    return coordinates_list
