import xlrd 
  
# Give the location of the file 
loc = ("data1.xlsx") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
  
# For row 0 and column 0 
print(sheet.cell_value(1, 0)) 
for i in range(1,sheet.nrows):
    print(sheet.cell_value(i,0),sheet.cell_value(i,1))
