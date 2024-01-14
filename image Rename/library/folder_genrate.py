import os
from os import listdir
from PIL import Image


# name_folder = input("Enter name folder :")

def creater_folder(urls,  name_folder): 
    # urls = '.\output'
    path = os.path.join(urls, name_folder)
    os.mkdir(path)
    return True

# creater_folder(urls,  name_folder)


# C:\Users\aditya.gupta\Documents\Tools Pack Final\Tools Pack Final\image Rename