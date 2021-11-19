import sys

import xlsxwriter



class create_excel():
    def __init__(self):
        pass

    def create__excel_ofData(self, table_name, fields, data):
        try:
            # Create a workbook and add a worksheet.
            workbook = xlsxwriter.Workbook("excel\\"+table_name + '.xlsx')
            worksheet = workbook.add_worksheet()

            # Some data we want to write to the worksheet.
            # fields = ["id", 'name', 'rollno']
            # data_list = [['1001', 'helly', '1'], ['1002', 'jack', '2'], ['1003', 'ram', '3']]
            row = 0
            col = 0
            for value in fields:
                worksheet.write(row, col, value)
                col += 1

            # Start from the first cell. Rows and columns are zero indexed.
            row = 1
            col = 0

            # Iterate over the data and write it out row by row.
            for row1 in data:
                col = 0

                for index in range(len(row1)):
                    worksheet.write(row, col, row1[index])
                    col += 1
                row += 1

            # Write a total using a formula.
            # worksheet.write(row, 0, 'Total')
            # worksheet.write(row, 1, '=SUM(B1:B4)')

            workbook.close()
            return "done"
        except:
            sys.exc_info()[1]



