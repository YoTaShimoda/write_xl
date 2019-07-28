import openpyxl

def write_xl(file,sheet,cell,value):
    file_name = file
    file = openpyxl.load_workbook(file)
    sheet = file[sheet]
    sheet[cell] = value
    file.save(file_name)
