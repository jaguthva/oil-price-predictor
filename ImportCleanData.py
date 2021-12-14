
################ Import weekly consumption data #########
import pandas as pd

excel_workbook = 'Petroleum_Consumption_Weekly.xlsx'
sheetname = 'Data 1'
sheet1 = pd.read_excel(excel_workbook, sheetname)
column_name_list = sheet1.columns.values

# Remove other subproducts from petroleum list -- only total petroleum products left
sheet1.drop(columns= column_name_list[2:], inplace = True)
#print(sheet1.columns.values)

print(sheet1.head(10))


# Import WTI Spot Prices from Cushing Oklahoma 
excel_workbook = 'WTI_Spot_Prices.xlsx'
sheetname = 'Data 1'
sheet2 = pd.read_excel(excel_workbook,sheetname)
print(sheet2.head(10))

matrix = pd.merge(sheet1, sheet2)

print(matrix.head(5))

