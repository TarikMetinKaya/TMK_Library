import requests

def urlShortener(URL,tinyUrlApiToken):
    try:
        url_main = f'https://api.tinyurl.com/create?api_token={tinyUrlApiToken}'
        myobj = {
          "url": URL,
          "domain": "tiny.one",
        }

        x = requests.post(url_main, data = myobj).json()

        return x['data']['tiny_url']
    except Exception as e:
        print(e)
        return URL
import pandas as pd
import math
import numpy as np

def dropUnnamedCol(df):
    """
    DF= col_1|col_2|Unnamed:1|Unnamed:2
        1    |42   |null     | null

    dropUnnamedCol(DF)
    OUTPUT:
    col_1|col_2
    1    |42


    :param df: DataFrame which you want to filter
    :return:
    """
    list_of_col=[]
    for col in df.columns:
        if not str(col).__contains__('Unnamed'):
            list_of_col.append(col)
    return df[list_of_col]


def dfNanDropper(dataFrame,ColumnName):
    """
    Usage:
    DF= col_1|col_2|col_3|col_4
        1    |42   |NaN  |Nan
        5    |23   |12   |Nan

    dfNanDropper(DF,"col_3")

    OUTPUT:
    col_1|col_2|col_3|col_4
    5    |23   |12   |Nan

    :param dataFrame: Dataframe
    :param ColumnName:  Name of column which is you want to drop nan values
    :return:
    """

    for i in range(0, len(dataFrame)):
        try:
            if math.isnan(dataFrame[ColumnName][i]):
                limit = i
                break
        except TypeError:
            if pd.isnull(dataFrame[ColumnName][i]):
                limit = i
                break

    for i in range(0, len(dataFrame)):
        if i >= limit:
            dataFrame = dataFrame.drop(index=i)
    return dataFrame


from datetime import datetime
from datetime import timedelta

def twoStringDateLength(start_date,end_date,is_end_date_include=True):
    """
    Usage:
    twoStringDateLength("2021-09-20","2021-09-21",False)
    OUTPUT: 1


    twoStringDateLength("2021-09-20","2021-09-21",True)
    OUTPUT: 2

    twoStringDateLength("2021-05-21","2021-05-15",False)
    OUTPUT: -6


    :param start_date: Must be like "%Y-%m-%d" string
    :param end_date: Must be like "%Y-%m-%d" string
    :param is_end_date_include: If it is True add last day to length
    :return:
    """

    start_date = datetime.strptime(start_date,"%Y-%m-%d")
    end_date = datetime.strptime(end_date,"%Y-%m-%d")
    delta = end_date - start_date
    if is_end_date_include:
        return delta.days+1
    else:
        return delta.days

def divide_date_range(start_date,end_date,divide_per_day):
    length=twoStringDateLength(start_date,end_date,True)
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    mod_minus=(length%divide_per_day)-1
    if mod_minus < 0:
        mod_minus=0
    normal_count=int(length/divide_per_day)
    start_dates_list=[]
    end_dates_list=[]
    temp_date=start_date
    start_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    for i in range(0,normal_count):
        temp_date=temp_date + timedelta(days=divide_per_day-1)
        end_dates_list.append(temp_date.strftime("%Y-%m-%d"))
        temp_date=temp_date + timedelta(days=1)

        start_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    temp_date=temp_date + timedelta(days=mod_minus)
    end_dates_list.append(temp_date.strftime("%Y-%m-%d"))
    return start_dates_list,end_dates_list

def deleteValueFromAllList(list, element):
    """
    Usage:
    a=[1,4,2,5,1,1,1,2,6]
    deleteValueFromAllList(a,1)
    Output: [4,2,5,2,6]

    :param list: A list
    :param element: An element which is you want to delete from all list
    :return: Filtered List
    """
    list = [x for x in list if x != element]
    return list

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






def setStringLength(string,length,align:"left"):
    """

    :param string: A str which is you want to set length
    :param length: Integer
    :param align: left, mid or right
    :return:
    """

    real_str_len=len(string)
    if real_str_len<length:

        if align=="left":
            text_which_add=""
            for i in range(0,length-real_str_len):
                text_which_add += " "
            return string + text_which_add

        elif align=="right":
            text_which_add = ""
            for i in range(0, length - real_str_len):
                text_which_add += " "
            return text_which_add + string

        elif align=="mid":
            left_text=""
            rigth_text=""
            for i in range(0, (length - real_str_len)):
                if i%2==0:
                    left_text += " "
                elif i%2==1:
                    rigth_text += " "
            return left_text + string + rigth_text

        if align not in ("left", "mid", "right"):
            print("Align must be \"left\", \"mid\" or \"right\" !!")
            return



    elif real_str_len>length:

        if align=="left":
            return string[0:length]
        elif align=="right":
            return string[-(length):]
        elif align=="mid":
            mid_index_of_text=int(real_str_len/2)
            if length%2==0:
                left_length=int(length/2)
                rigth_length=int(length/2)
            elif length%2==1:
                left_length=int(length/2)+1
                rigth_length=int(length/2)

            var_x=int(mid_index_of_text-left_length+1)
            var_y=int(mid_index_of_text+rigth_length+1)

            return string[var_x:var_y]
        if not align in ("left", "mid", "right"):
            print("Align must be \"left\", \"mid\" or \"right\" !!")
            return

def addCharOnString(string,char,amount,type:"pre-post"):
    """

    :param string: Text is which you want to add smth pre, post or both
    :param char: Must be just one character
    :param amount: int
    :param type: pre, post, pre-post
    :return:
    """
    if type not in ("pre","post","pre-post"):
        print("Type must be \"pre\", \"post\" or \"pre-post\" !!")
        return
    if not len(char)==1:
        print("Lenght of char must be 1")
    text_which_add=""
    for i in range(0,amount):
        text_which_add += f"{char}"
    if type == "pre":
        return text_which_add+string
    elif type == "post":
        return string+text_which_add
    elif type == "pre-post":
        return text_which_add+string+text_which_add

