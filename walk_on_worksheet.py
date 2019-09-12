import openpyxl

wb = openpyxl.load_workbook('example.xlsx')
sheet = wb['Sheet1']

for rowOfCells in sheet['A1':'C3']:
	for cell in rowOfCells:
		print(cell.coordinate, cell.value)
	print('--- END OF ROW ---')
