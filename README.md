This area will be update



import os
import configScript


def getFilesFromFolderAsList(folder_loc,file_extension):
    """
    Example:
        >>> location="Users/Project/File"

        >>> getFilesFromFolderAsList(location,"jpg")
        >>> getFilesFromFolderAsList(location,"pdf")
        >>> getFilesFromFolderAsList(location,"*")

    :param folder_loc: Folder location where is you want to read files from.
    :param file_extension: Extension which is you want to read files. If you want to read all files you can use "*".
    :return: List of Files
    """
    if file_extension=="*":
        list_of_files=os.listdir(folder_loc)
    else:
        list_of_files=list(filter(lambda name: name[-(len(file_extension)):] == file_extension, os.listdir(folder_loc)))

    return list_of_files
