import csv
import linecache
from shutil import copyfile

from Bunch import Bunch
from image_utils import get_img_list, get_img_path_name_frm_index, get_file_name


def merge_dirs_csvs(path_objs, out_dir, extension):
    # dict ={}
    img_counter = 1
    merged_csv_file = open(out_dir + '//' + 'groundTruth.csv', 'w')
    writer = csv.writer(merged_csv_file, delimiter=',')
    for item in path_objs:
        row_list = []
        csv_line_counter = 1
        for old_img_path in get_img_list(item.dir_path, extension):
            new_img_path, new_img_name = get_img_path_name_frm_index(img_counter, out_dir)
            copyfile(old_img_path, new_img_path)
            row = linecache.getline(item.csv_path, csv_line_counter).replace(get_file_name(old_img_path), new_img_name)
            # dict[get_file_name(old_img_path)] = new_img_name
            row_list.append([row])
            img_counter += 1
            csv_line_counter += 1
        for line in row_list:
            writer.writerow(line)
    merged_csv_file.close()


lbunchs = []
lbunchs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/base',
                     csv_path='/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/base/base.csv'))
lbunchs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/bright',
                     csv_path='/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/bright/bright.csv'))

out_dir = '/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/result'
merge_dirs_csvs(lbunchs, out_dir, 'png')
