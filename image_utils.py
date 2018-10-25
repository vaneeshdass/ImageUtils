import glob
import os

from config import get_config_object


def get_file_number(file_name):
    file_dir, file_name = os.path.split(file_name)
    file_no, file_ext = os.path.splitext(file_name)
    return file_no


def get_file_name(file_path):
    file_dir, file_name = os.path.split(file_path)
    return file_name


def get_width_height_img(img):
    height, width, channels = img.shape
    return width, height


def get_txt_path_name_frm_index(txt_index, out_dir):
    txt_name = "%6.6d.txt" % (txt_index)
    txt_path = os.path.join(out_dir, txt_name)
    return txt_path, txt_name


def get_img_path_name_frm_index(img_index, out_dir):
    img_name = get_config_object()['FileFormat']['ImageFormat'] % (img_index)
    img_path = os.path.join(out_dir, img_name)
    return img_path, img_name


def get_img_list(in_dir, ext, is_srt=True):
    src_dir = in_dir + '/*.' + ext
    list_images = glob.glob(src_dir)
    if is_srt:
        list_images.sort()
    return list_images
