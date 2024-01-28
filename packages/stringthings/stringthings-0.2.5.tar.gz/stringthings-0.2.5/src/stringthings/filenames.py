# -*-coding: utf-8 -*-
"""
Created on Mon Jan 01 13:53:33 2024

@author: Martín Araya
"""
from os.path import isfile, isdir, exists

__all__ = ['extension']


def extension(file_path: str, backslash_to_slash=True, back_compatibility=False):
    """
    receives a string indicating a FileName.Extension or
    Path/FileName.Extension and return a tuple containing
    [0] the .Extension of the file in filepath,
    [1] the name of the FileName without extension_,
    [2] the Directory containing the file,
    [3] the fullpath

    in case an item is not present an empty string is returned by default.
    """

    file_path = file_path.strip()

    if bool(backslash_to_slash) is True:
        file_path = file_path.replace('\\', '/')

    if '/' in file_path:
        len_path = len(file_path) - file_path[::-1].index('/')
        path_ = file_path[:len_path]
    else:
        len_path = 0
        path_ = ''

    if '.' in file_path[len_path:]:
        file_name_ = file_path[len_path:len(file_path) - file_path[::-1].index('.') - 1]
        extension_ = file_path[len(file_path) - file_path[::-1].index('.') - 1:]
    else:
        file_name_ = file_path[len_path:]
        extension_ = ''

    fullpath_ = f"{path_}{file_name_}{extension_}".strip()
    if not isfile(fullpath_) and extension_ == '':
        file_name_, extension_, path_= '', '', f"{path_}{file_name_}{extension_}"

    if back_compatibility:
        return file_name_, extension_, path_, fullpath_
    else:
        return extension_, file_name_, path_, fullpath_
