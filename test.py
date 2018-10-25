from csv_to_yolo import convert_csv_to_yolo_format

# region merge
# list_of_bunch_objs = []
# list_of_bunch_objs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/Base_and_Aug_Images_PNG',
#                                 csv_path='/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/base_norm_gt.csv'))
# list_of_bunch_objs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/bright/images',
#                                 csv_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/bright/groundTruth.csv'))
# list_of_bunch_objs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/patch_noise/images',
#                                 csv_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/patch_noise/groundTruth.csv'))
# list_of_bunch_objs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/skew_10/images',
#                                 csv_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/skew_10/groundTruth.csv'))
# list_of_bunch_objs.append(Bunch(dir_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/skew_-10/images',
#                                 csv_path='/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/skew_-10/groundTruth.csv'))
#
# out_dir_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/all_25k/images'
# merge_dirs_csvs(list_of_bunch_objs, out_dir_path)

# endregion

# region csvToYolo
# in_dir = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/all_25k/images'
# out_dir = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/25k_yolo'
# csv_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/all_25k/groundTruth.csv'
# convert_csv_to_yolo_format(in_dir, out_dir, csv_path)
# endregion

# in_dir = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/all_25k'

# region noiseGenerate
# in_dir = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/Base_and_Aug_Images_PNG'
# out_dir = '/home/vaneesh/Drive/ML/Datasets/Mastif/25_k_dataset/patch_noise/images'
# csv_path = '/home/vaneesh/Drive/ML/Datasets/Mastif/Base_images/base_norm_gt.csv'
#
# generate_nois_patch_images_and_GT(in_dir, out_dir, csv_path)
# endregion

in_dir = '/media/vaneesh/Data/Datasets/German/training/training_5_classes (copy)/0/'
out_dir = '/media/vaneesh/Data/Datasets/German/training/training_5_classes (copy)/out'

convert_csv_to_yolo_format(in_dir, out_dir, 'augmentGTAll2.csv')
