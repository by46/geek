from cStringIO import StringIO
from datetime import datetime

import xlwt

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
                     num_format_str='#,##0.00')
style1 = xlwt.easyxf(num_format_str='D-MMM-YY')

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write_merge(0, 0, 0, 2, 1234.56, style0)
# ws.write(0, 0, 1234.56, style0)

ws.write(1, 0, datetime.now(), style1)
ws.write(2, 0, 1)
ws.write(2, 1, 1)
ws.write(2, 2, xlwt.Formula("A3+B3"))

io = StringIO()
wb.save(io)

with open('example.xls', 'wb') as writer:
    writer.write(io.getvalue())
