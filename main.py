
from utilities import *


def print_welcome():    
    print("Welcome to the Slot Machine!")
    print(f"Maximum lines: {MAX_LINES}")
    print(f"Maximum bet per line: ${MAX_BET}")  

def deposit():  
    amount  = GetAndValidateInput("Please enter amount to deposit. $", 1, 100000)   
    return amount

def get_number_of_lines():
    lines = GetAndValidateInput("Enter the number of lines to bet on (1-3): ", 1, MAX_LINES)
    return lines

def get_bet():
    bet = GetAndValidateInput(f"Enter your bet per line (${MIN_BET}-${MAX_BET}): ", MIN_BET, MAX_BET)
    return bet

def main():
    print_welcome()
    balance = deposit()
    print(f"You have successfully deposited ${balance}.")            
    lines = get_number_of_lines()
    print(f"You have chosen to bet on {lines} lines.")
    while True:
        bet = get_bet()
        print(f"You have chosen to bet ${bet} per line.")
        total_bet = bet * lines
        print(f"Your total bet is ${total_bet}.")
        if total_bet > balance:
            print(f"You do not have enough balance to place this bet. Your balance is ${balance}.")
        else:
            break
    print("Thank you for placing your bet!")
    balance -= total_bet

    print(f"Your remaining balance is ${balance}.")

    first_spin = True
    while True:
        if balance >= 0:
            play_again = input("Do you want to play? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y'] :
                columns = spin_slot_machine(ROWS, COLS, symbols)
               
                if not first_spin :
                    balance -= total_bet
                
                print(columns)
                print("Here are the results of your spin:")
                print_slot_machine(columns)
                winnings = GetWinnings(columns, bet, lines)
                print(f"You won ${winnings}!")
                balance += winnings
                print(f"Your new balance is ${balance}.")            
                first_spin = False
            elif play_again in ['no', 'n']:
                print("Thank you for playing! Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
       
        else:
            print("You have run out of balance. Thank you for playing!")        
            return
main()

