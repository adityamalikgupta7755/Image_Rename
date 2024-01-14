import os
from os import listdir
from PIL import Image
from .Rename_string import clean_string
from .Excelwrite import write_to_excel



def Write_img_name_excel(urls, Excel_file_path):
    data = [['count', 'Name of image ', 'New Name'],]
    count = 0
    for images in (os.listdir(urls)):
        a_list=[]
        if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
            img_name=images.split(".")[0]
            a_list.append(count)
            a_list.append(img_name)
            a_list.append(clean_string(img_name))
            count=count+1
            data.append(a_list)
    result = write_to_excel(Excel_file_path, 'Sheet1', data)
    return result

    

 

