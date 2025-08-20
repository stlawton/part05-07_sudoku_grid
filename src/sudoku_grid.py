def row_correct(sudoku: list, row_no: int):
  row_size = len(sudoku[row_no]) # Store row size in variable
  number = 1
  while number <= row_size: # Iterate across row
    if number in sudoku[row_no]:
      if sudoku[row_no].count(number) > 1:
        return False
    number += 1
  return True

def column_correct(sudoku: list, column_no: int):
  column_length = len(sudoku) # column length is the same as the number of rows in sudoku
  number = 1 # Variable will be used to check for each number 1-9
  while number <= column_length:
    row = 0 # Variable to move through each row
    count = 0
    while row < column_length:
      if number == sudoku[row] [column_no]: # Check to see if numbers 1-9 are in the column
        count += 1
      row += 1
    if count > 1:
        return False
    number += 1
  return True # If loop completes then each number was found only once in the column, return true.

def block_correct(sudoku: list, row_no: int, column_no: int):
  checked_numbers = []
  number = 1
  while number < 10:
    for i in range(row_no, row_no + 3):
      for j in range(column_no, column_no + 3):
        if number == sudoku[i][j]:
          if checked_numbers.count(number) < 1:
            checked_numbers.append(number)
          else:
            return False
    number += 1
  return True

def sudoku_grid_correct(sudoku: list):
  row = 0
  column = 0
  while row < 10:
    if row_correct(sudoku, index) == False:
      return False
    if column_correct(sudoku, index) == False:
      return False
  for i in range(0, 7, 3):
    for j in range(0, 7, 3):
      if block_correct(sudoku, i, j) == False:
        return False
  return True
