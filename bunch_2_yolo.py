from image_utils import get_width_height_img


# This function returns the list of coordinates in yolo format
def get_yolo_llist(list_bunch_instances, img):
    llist_yolo = []
    img_w, img_h = get_width_height_img(img)
    inv_imgw = 1 / img_w
    inv_imgh = 1 / img_h

    for instance in list_bunch_instances:
        x_min, y_min, x_max, y_max, lbl = instance.x_min, instance.y_min, instance.x_max, instance.y_max, instance.lbl
        x_yolo = ((x_min + x_max) / 2) * inv_imgw
        y_yolo = ((y_min + y_max) / 2) * inv_imgh
        w_yolo = (x_max - x_min) * inv_imgw
        h_yolo = (y_max - y_min) * inv_imgh
        tmp_list = [lbl, x_yolo, y_yolo, w_yolo, h_yolo]
        llist_yolo.append(tmp_list)

    return llist_yolo
