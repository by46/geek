from datetime import datetime

import xlwt

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on; align: horiz center, vert center, wrap on',
                     num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')
print ws.col(0).width
print ws.col(1).width
print ws.col(2).width
ws.col(0).width = 367*20

ws.write(0, 0, 1234.56, style0)
ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))
ws.write_merge(3,4,0, 3, "Long Cell xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", style0)

wb.save('example.xls')
