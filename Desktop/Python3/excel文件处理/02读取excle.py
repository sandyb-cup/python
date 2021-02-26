import openpyxl
wb = openpyxl.load_workbook("music.xlsx")
sheet = wb["xxxx"]
sheethame = wb.sheetnames
print(sheethame)
A1_value = sheet["A1"].value
print(A1_value)


