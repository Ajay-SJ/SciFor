import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'

        for i in range(3):
            for j in range(3):
                button = tk.Button(self.window, text='', command=lambda i=i, j=j: self.click(i, j), height=3, width=6)
                button.grid(row=i, column=j)
                self.board[i*3+j] = button

    def click(self, i, j):
        if self.board[i*3+j]['text'] == '':
            self.board[i*3+j]['text'] = self.current_player
            if self.check_win():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            if self.current_player == 'O':
                self.computer_move()

    def computer_move(self):
        empty_cells = [i for i, cell in enumerate(self.board) if cell['text'] == '']
        if empty_cells:
            cell = random.choice(empty_cells)
            self.board[cell]['text'] = 'O'
            if self.check_win():
                messagebox.showinfo("Game Over", "Computer wins!")
                self.window.quit()
            self.current_player = 'X'

    def check_win(self):
        win_conditions = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        for condition in win_conditions:
            if self.board[condition[0]]['text'] == self.board[condition[1]]['text'] == self.board[condition[2]]['text'] != '':
                return True
        return False

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
