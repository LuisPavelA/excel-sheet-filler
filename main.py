import openpyxl as xl

# Variables

# File
original_worksheet = "Empty.xlsx"

# Experiment Variables
experiment_num = 1
iteration_num = 1

# Sheet Coverage
column_start = 1
column_end = 10

row_start = 1
row_end = 10

# Value
new_cell_value = "Test"

# Other
printing = True





wb = xl.load_workbook(original_worksheet)
sheet = wb["Sheet1"]


for row in range(row_start, row_end):
  for column in range(column_start, column_end):
    cell = sheet.cell(row, column)
    cell.value = new_cell_value
    if printing == True:
      print(f"Row {row} and Column {column}")

wb.save(f"Experiment_{experiment_num}_{iteration_num}.xlsx")