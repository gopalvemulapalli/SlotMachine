import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbols = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1
}

def spin_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)
    
    columns = []
    if rows <= 0 or cols <= 0:
        raise ValueError("Rows and columns must be greater than zero.")

    for _ in range(cols):
        column = []
        for _ in range(rows):  
            symbol = all_symbols.pop(random.randint(0, len(all_symbols) - 1))
            column.append(symbol)

        columns.append(column)           
    
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,col in enumerate(columns):
            if i == len(columns) - 1:
                print(col[row], end="")
            else:
                print(col[row], end=" | ")
        print()  # New line after each row
    print()  # Extra new line for better readability

def GetWinnings(columns, bet, lines):
    winnings = 0
    for i in range(lines):
        if columns[i][0] == columns[i][1] == columns[i][2]:  # Check if all symbols in the line are the same
            winnings += bet * symbols[columns[i][0]]  # Multiply bet by the symbol's value
    return winnings

def GetAndValidateInput(prompt, min_value, max_value):
    while True:
        value = input(prompt)
        if value.isdigit():
            value = int(value)
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        else:
            print("Invalid input. Please enter a valid number.")
    
