import xlsxwriter

 

def write_to_excel(filename, sheet_name, data):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(sheet_name)
    for row_num, row_data in enumerate(data):
        for col_num, cell_value in enumerate(row_data):
            worksheet.write(row_num, col_num, cell_value)

    workbook.close()
    return True

 

# Example usage:
# data = [
#     ['Name', 'Age', 'Country'],
#     ['John', 30, 'USA'],
#     ['Alice', 25, 'Canada'],
#     ['Bob', 35, 'UK']
# ]

 

# write_to_excel('image.xlsx', 'Sheet1', data)