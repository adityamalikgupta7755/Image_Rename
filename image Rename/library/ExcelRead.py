import openpyxl

 

def read_excel(filename, sheet_name):
    try:
        workbook = openpyxl.load_workbook(filename)
        worksheet = workbook[sheet_name]
        data = []
        for row in worksheet.iter_rows(values_only=True):
            data.append(list(row))

 

        return data
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None

 

# Example usage:

# file_name='.\output\image.xlsx'

# file_data = read_excel(file_name, 'Sheet1')
# if file_data:
#     count=0
#     for row in file_data:
#         print(f"{count}  {row}")
#         count=count+1