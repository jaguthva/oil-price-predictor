# Import weekly consumption data
import pandas as pd

excel_workbook = 'Petroleum_Consumption_Weekly.xlsx'
sheetname = 'Data 1'
sheet1 = pd.read_excel(excel_workbook, sheetname)

print(sheet1.head(10))