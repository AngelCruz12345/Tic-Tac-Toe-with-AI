
import tkinter as tk
from tkinter import messagebox
import math

# Game board
board = [" " for _ in range(9)]
buttons = []

# Check for a winner
def check_winner(player):
    winning_combinations = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_combinations:
        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check if board is full
def board_full():
    return " " not in board


# Minimax algorithm
def minimax(is_maximizing):
    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score


# Computer makes its move
def computer_move():
    best_score = -math.inf
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    if best_move is not None:
        board[best_move] = "O"
        buttons[best_move].config(
            text="O",
            fg="#ef4444"
        )


# Check if game is finished
def check_game_over():
    if check_winner("X"):
        status_label.config(text="You Win!")
        messagebox.showinfo("Game Over", "You Win!")
        return True

    if check_winner("O"):
        status_label.config(text="Computer Wins!")
        messagebox.showinfo("Game Over", "Computer Wins!")
        return True

    if board_full():
        status_label.config(text="It's a Tie!")
        messagebox.showinfo("Game Over", "It's a Tie!")
        return True

    return False


# Player clicks a button
def player_move(index):
    if board[index] != " ":
        return

    if check_winner("X") or check_winner("O"):
        return

    board[index] = "X"

    buttons[index].config(
        text="X",
        fg="#3b82f6"
    )

    if check_game_over():
        return

    status_label.config(text="Computer's Turn")

    computer_move()

    if check_game_over():
        return

    status_label.config(text="Your Turn (X)")


# Restart the game
def restart_game():
    global board

    board = [" " for _ in range(9)]

    for button in buttons:
        button.config(text=" ")

    status_label.config(text="Your Turn (X)")


# Create the window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="#1e293b")

# Title
title_label = tk.Label(
    root,
    text="TIC-TAC-TOE",
    font=("Arial", 26, "bold"),
    bg="#1e293b",
    fg="white"
)
title_label.pack(pady=20)

# Status
status_label = tk.Label(
    root,
    text="Your Turn (X)",
    font=("Arial", 16),
    bg="#1e293b",
    fg="white"
)
status_label.pack(pady=10)

# Frame for the board
board_frame = tk.Frame(
    root,
    bg="#1e293b"
)
board_frame.pack(pady=15)

# Create the 9 buttons
for i in range(9):
    button = tk.Button(
        board_frame,
        text=" ",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        bg="white",
        command=lambda i=i: player_move(i)
    )

    button.grid(
        row=i // 3,
        column=i % 3,
        padx=3,
        pady=3
    )

    buttons.append(button)


# Restart button
restart_button = tk.Button(
    root,
    text="Restart Game",
    font=("Arial", 14, "bold"),
    bg="#22c55e",
    fg="white",
    command=restart_game
)
restart_button.pack(pady=15)

# Start the GUI
root.mainloop()
