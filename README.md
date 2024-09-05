# Slot Machine Game with Tkinter

A simple slot machine game implemented in Python using the Tkinter library for the graphical user interface (GUI). This game allows users to deposit money, place bets on multiple lines, and spin the slot machine to try their luck!

## Purpose of the Project

This project was created specifically to strengthen my concepts of Python programming. It covers fundamental topics such as functions, loops, conditionals, error handling, and GUI development with Tkinter.

## Features

- User-friendly GUI built with Tkinter.
- Allows players to deposit money into their balance.
- Players can choose the number of lines to bet on (1 to 3).
- Players can set a bet amount for each line (between $1 and $100).
- Displays the slot machine results and calculates winnings.
- Provides real-time feedback on invalid input or insufficient balance.

## Technologies Used

- **Python**: The core programming language for implementing the game logic.
- **Tkinter**: A standard GUI library in Python to create the graphical interface.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/Sambhav-Maheshwari/Slot-Machine
    ```

2. **Install Python (if not already installed):**

    Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

3. **Run the Game:**

    Execute the following command to start the game:

    ```bash
    python slot-machine.py
    ```

## How to Play

1. **Deposit Money:**
   - Enter the amount you want to deposit in the "Deposit Amount" field and click the "Deposit" button.

2. **Place Your Bet:**
   - Enter the number of lines you want to bet on (between 1 and 3) in the "Number of Lines" field.
   - Enter the amount you want to bet on each line (between $1 and $100) in the "Bet Amount" field.

3. **Spin the Slot Machine:**
   - Click the "Spin" button to spin the slot machine.
   - The results will be displayed on the screen, showing the symbols and indicating any winnings.

4. **Repeat or Quit:**
   - Continue to play by adjusting your bet or deposit more money.
   - Close the application window to quit the game.

## Rules

- You can bet on up to 3 lines simultaneously.
- The bet amount for each line must be between $1 and $100.
- The total bet is the number of lines multiplied by the bet amount.
- If the symbols on a line match, you win based on the symbol values:
  - **A**: 5x the bet amount
  - **B**: 4x the bet amount
  - **C**: 3x the bet amount
  - **D**: 2x the bet amount

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you want to improve the game or fix any bugs.

## Acknowledgments

- Special thanks to the Python and Tkinter communities for providing great resources and tutorials.
- Inspiration from classic slot machine games.

---

Enjoy the game, and good luck!
