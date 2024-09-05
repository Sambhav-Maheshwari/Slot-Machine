import random
import tkinter as tk
from tkinter import messagebox

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += bet * values[symbol]
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


def print_slot_machine(columns, result_labels):
    for row in range(len(columns[0])):
        result_text = ""
        for i, column in enumerate(columns):
            result_text += column[row]
            if i != len(columns) - 1:
                result_text += " | "
        result_labels[row].config(text=result_text)


def spin():
    global balance
    try:
        bet = int(bet_entry.get())
        lines = int(lines_entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for bet and lines.")
        return

    if not (MIN_BET <= bet <= MAX_BET):
        messagebox.showerror("Invalid Bet", f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        return

    if not (1 <= lines <= MAX_LINES):
        messagebox.showerror("Invalid Lines", f"Lines must be between 1 and {MAX_LINES}.")
        return

    total_bet = bet * lines

    if total_bet > balance:
        messagebox.showerror("Insufficient Balance", "You don't have enough balance to place this bet.")
        return

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots, result_labels)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

    result_label.config(text=f"Your winnings: ${winnings}\nWinning lines: {winning_lines}")
    balance += winnings - total_bet
    balance_label.config(text=f"Current Balance: ${balance}")


def deposit():
    global balance
    try:
        deposit_amount = int(deposit_entry.get())
        if deposit_amount <= 0:
            messagebox.showerror("Invalid Amount", "Deposit amount must be greater than 0.")
            return
        balance += deposit_amount
        balance_label.config(text=f"Current Balance: ${balance}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")


# Create main window
root = tk.Tk()
root.title("Slot Machine Game")

balance = 0

# GUI Elements
balance_label = tk.Label(root, text=f"Current Balance: ${balance}")
balance_label.grid(row=0, column=0, columnspan=3)

deposit_label = tk.Label(root, text="Deposit Amount:")
deposit_label.grid(row=1, column=0)
deposit_entry = tk.Entry(root)
deposit_entry.grid(row=1, column=1)
deposit_button = tk.Button(root, text="Deposit", command=deposit)
deposit_button.grid(row=1, column=2)

lines_label = tk.Label(root, text="Number of Lines (1-3):")
lines_label.grid(row=2, column=0)
lines_entry = tk.Entry(root)
lines_entry.grid(row=2, column=1)

bet_label = tk.Label(root, text="Bet Amount (1-100):")
bet_label.grid(row=3, column=0)
bet_entry = tk.Entry(root)
bet_entry.grid(row=3, column=1)

spin_button = tk.Button(root, text="Spin", command=spin)
spin_button.grid(row=4, column=0, columnspan=3)

result_labels = [tk.Label(root, text="") for _ in range(ROWS)]
for i, label in enumerate(result_labels):
    label.grid(row=5 + i, column=0, columnspan=3)

result_label = tk.Label(root, text="")
result_label.grid(row=8, column=0, columnspan=3)

root.mainloop()
