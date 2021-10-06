import os
import random
import shutil
from time import sleep

def randomMixerTrainAndTestFiles(images_extension:"jpg",labels_extension:"xml",images_loc,labels_loc,train_loc,test_loc,train_ratio:.95):
    """
    Usage:
    IMAGES_PATH="/project/allImages"
    LABELS_PATH="/project/allLabels"
    TRAIN_PATH="/project/trainFolder"
    TEST_PATH="/project/testFolder"
    randomMover("jpg",
                "xml",
                IMAGES_PATH,
                LABELS_PATH,
                TRAIN_PATH,
                TEST_PATH,
                .90)

    :param images_extension: Like "jpg", "png", "jpeg" WITHOUT DOT (.)
    :param labels_extension: Like "xml" WITHOUT DOT (.)
    :param images_loc: Location, where is you stored your images, Images and labels must be same names
    :param labels_loc: Location, where is you stored your labels, Images and labels must be same names
    :param train_loc: Train folder location
    :param test_loc: Test folder location
    :param train_ratio: (Train Files Count)/(Test Files Count) ratio
    :return:
    """
    list_of_images = list(filter(lambda name: name[-3:]==images_extension, os.listdir(images_loc)))
    list_of_labels = list(filter(lambda name: name[-3:] == labels_extension, os.listdir(labels_loc)))
    list_of_images.sort()
    list_of_labels.sort()
    list_of_file_names=[]
    for f in list_of_images:
        list_of_file_names.append(f[:(-1)*(len(images_extension))-1])
    print("Your File names: "+str(list_of_file_names))
    print("Your Images: "+str(list_of_images))
    print("Your Labels: "+str(list_of_labels))
    if not len(list_of_labels)==len(list_of_images):
        print("Labels and Images files is not matching, please check it and try again.")
        return

    test_count=int(len(list_of_file_names)*(1-train_ratio))
    train_count=len(list_of_file_names)-test_count
    print(f"Train Count: {train_count}, Test Count: {test_count}")

    print("Cleaning your Train and Test locations in 5 sec...")
    sleep(1)
    print("Cleaning your Train and Test locations in 4 sec...")
    sleep(1)
    print("Cleaning your Train and Test locations in 3 sec...")
    sleep(1)
    print("Cleaning your Train and Test locations in 2 sec...")
    sleep(1)
    print("Cleaning your Train and Test locations in 1 sec...")
    sleep(1)
    print("Cleaning your Train and Test locations in 0 sec...")
    for f in os.listdir(train_loc):
        os.remove(os.path.join(train_loc, f))
    for f in os.listdir(test_loc):
        os.remove(os.path.join(test_loc, f))
    print("Cleaned your Train and Test locations.")

    test_list=random.sample(list_of_file_names,test_count)
    print("Selected random test files: "+str(test_list))

    print("Copying train and test files to locations...")
    for f_name in test_list:
        shutil.copyfile(images_loc+f"\\{f_name}.{images_extension}",test_loc+f"\\{f_name}.{images_extension}")
        shutil.copyfile(labels_loc+f"\\{f_name}.{labels_extension}",test_loc+f"\\{f_name}.{labels_extension}")
    for oth_f in list(set(list_of_file_names)-set(test_list)):
        shutil.copyfile(images_loc + f"\\{oth_f}.{images_extension}", train_loc + f"\\{oth_f}.{images_extension}")
        shutil.copyfile(labels_loc + f"\\{oth_f}.{labels_extension}", train_loc + f"\\{oth_f}.{labels_extension}")
    print("Copied all files")





