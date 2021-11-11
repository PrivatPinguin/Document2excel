# xls Writer

# Writing to an excel 
# sheet using Python
import xlwt
from xlwt import Workbook
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(0, 0, 'A1')
sheet1.write(0, 1, 'A2')
sheet1.write(1, 0, 'B1')
sheet1.write(1, 1, 'B2')

wb.save('xlwt_tst.xls')
