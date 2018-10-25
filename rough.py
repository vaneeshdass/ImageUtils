import csv

with open('/home/vaneesh/Drive/ML/VishalSharedFIles/optimizedCode/ImgUtils/test/sample.csv', 'r') as src_csv_file:
    csv_src_rows = csv.reader(src_csv_file, delimiter=',')
    # for row in csv_src_rows:
    print(csv_src_rows[0][0])


def deflate_bunch_in_list(img_name, no_instances, coordinates_list):
    li = []
    for item in coordinates_list:
        x_min, y_min, x_max, y_max, lbl = item.x_min, item.y_min, item.x_max, item.y_max, item.lbl
        li.extend((x_min, y_min, x_max, y_max, lbl))
    li.insert(0, img_name)
    li.insert(1, no_instances)
    return li
