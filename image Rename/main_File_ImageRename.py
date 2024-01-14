from library.image_name_to_Excle import Write_img_name_excel
from library.Rename_img import rename_img




Excel_file_path='.\output\image.xlsx'

flag = True

while flag:
    message = """ 
    Welcome to Image Rename Created By AMG
    The Image rename is a 2-step Process
    Step 1: Read all images from a folder and write to an Excel Sheet. Enter no -> 1
    Step 2: Open image.xlsx Excel file and check if names are correct.
    Step 3: Rename the images. Enter no -> 2
    Step 4: Exit. Enter no -> 3
    """
    print(message)
    try:
        selection = int(input("Enter Option no: "))
        if selection ==  1 or selection == 2:
            original_urls_path = input("Enter oringinal image folder path:")
            if selection == 1:
                if Write_img_name_excel(original_urls_path, Excel_file_path):
                    print("Please Check output folder")
            elif selection == 2:
                new_folder_name = input("Enter new folder name:")
                if rename_img(original_urls_path, new_folder_name, Excel_file_path):
                    print("all image Renamed")
        elif selection == 3:
            flag = False
        else:
            print("Invalid selection. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")











