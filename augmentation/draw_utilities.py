import cv2


def draw_rectangle(row, img_path):
    # global test_counter
    img = cv2.imread(img_path)
    counter = 2
    no_of_instances = int(row[1])
    for ii in range(no_of_instances):
        x1 = int(row[counter])
        counter += 1
        y1 = int(row[counter])
        counter += 1
        width = int(row[counter])
        counter += 1
        height = int(row[counter])
        counter += 1
        cv2.rectangle(img, (x1, y1), (width, height), (0, 255, 0), 3)
        cv2.imwrite(img_path, img)
