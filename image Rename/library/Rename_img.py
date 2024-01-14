from .ExcelRead import read_excel
from .folder_genrate import creater_folder
import os
from os import listdir
from PIL import Image



# original_urls_path = input("Enter oringinal image folder path:")
# new_folder_name = input("Enter new folder name:")
# Excel_file_path='.\output\image.xlsx'


def rename_img(original_urls_path, new_folder_name, Excel_file_path):
    new_folder_urls_path = os.path.dirname(original_urls_path)
    file_data = read_excel(Excel_file_path, 'Sheet1')
    if file_data:
        a = file_data.pop(0)
        print("a", a)
    if creater_folder(new_folder_urls_path, new_folder_name):
        count = 0
        for  images in  (os.listdir(original_urls_path)):
            if (images.endswith(".png") or images.endswith(".jpg") or images.endswith(".jpeg")):
                if count == int(file_data[count][0]):
                    if (images.split("."))[0] == file_data[count][1]:
                        print("count", count)
                        print("file_data[count][0]", file_data[count][1])
                        print("images", (images.split("."))[0])
                        print("file_data", file_data[count])
                 
                        orignal_url_of_img =f"{original_urls_path}\\\\{images}"
                        new_url_of_img =f"{new_folder_urls_path}\\\\{new_folder_name}\\\\{file_data[count][2]}.png"
                        im1 = Image.open(orignal_url_of_img)
                        im2 = im1.copy()
                        im2.save(new_url_of_img)
                        pr = f"{file_data[count][2]}.png"
                        print(pr,"file saved") 
                        count=count+1
        return True

# if rename_img(original_urls_path, new_folder_name, Excel_file_path):
#     print("all image Renamed")