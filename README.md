# Excel Sheet Filler
## A python script that fills an Excel sheet with a string.

# How to run
## 1. You need to have Python on your computer.

## 2. You need to install **openpyxl**.
### You do that by running this code in your terminal:
```
pip install openpyxl
```

## 3. Then you need to customize the settings to your needs
```py
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
```
### This settings can be found at the top of the `main.py` file

## 4. Then you need to run the file by running this in your terminal
```py
py main.py
```

# Credits
## Original Code from [Programming With Mosh](https://www.youtube.com/watch?v=_uQrJ0TkZlc&t=14134s) and updated by [Luis Pavel](https://luispavel.web.app/)
