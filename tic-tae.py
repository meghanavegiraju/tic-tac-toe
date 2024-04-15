
import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        
        # Create a 3x3 grid of buttons for the game board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.current_mark = 'X'  # Start with player 'X'
        
        # Create buttons and place them in the grid
        for row in range(3):
            for col in range(3):
                button = tk.Button(master, text=' ', font=('Helvetica', 20), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Initialize the game board and status
        self.game_over = False
        self.reset_game()
    
    def on_button_click(self, row, col):

        if not self.game_over and self.buttons[row][col].cget('text') == ' ':
        # Player's turn: mark the button with 'X'
            self.buttons[row][col].config(text=self.current_mark)
        
        # Check if the current player has won
        if self.check_winner():
            self.show_winner(self.current_mark)
            self.game_over = True
            return
        elif self.is_board_full():
            self.show_draw()
            self.game_over = True
            return
        
        # Switch turns: change mark from 'X' to 'O'
        self.current_mark = 'O'
        self.master.after(500, self.computer_move)

    
    def computer_move(self):
        """Make a move for the computer (player 'O')."""
        if not self.game_over:
            # Find available cells
            available_cells = [(r, c) for r in range(3) for c in range(3) if self.buttons[r][c].cget('text') == ' ']
            
            if available_cells:
                # Choose a random available cell
                row, col = random.choice(available_cells)
                
                # Make the move (computer's turn)
                self.buttons[row][col].config(text=self.current_mark)
                
                # Check if the computer has won
                if self.check_winner():
                    self.show_winner(self.current_mark)
                    self.game_over = True
                    return
                
                # Check if the board is full
                if self.is_board_full():
                    self.show_draw()
                    self.game_over = True
                    return
                
                # Switch turns back to the player
                self.current_mark = 'X'

    def check_winner(self):
        """Check if there is a winner."""
        # Check rows and columns
        for i in range(3):
            if (self.buttons[i][0].cget('text') == self.buttons[i][1].cget('text') == self.buttons[i][2].cget('text') != ' ') or \
               (self.buttons[0][i].cget('text') == self.buttons[1][i].cget('text') == self.buttons[2][i].cget('text') != ' '):
                return True
        
        # Check diagonals
        if (self.buttons[0][0].cget('text') == self.buttons[1][1].cget('text') == self.buttons[2][2].cget('text') != ' ') or \
           (self.buttons[0][2].cget('text') == self.buttons[1][1].cget('text') == self.buttons[2][0].cget('text') != ' '):
            return True
        
        return False
    
    def is_board_full(self):
        """Check if the board is full."""
        for row in range(3):
            for col in range(3):
                if self.buttons[row][col].cget('text') == ' ':
                    return False
        return True
    
    def reset_game(self):
        """Reset the game board for a new game."""
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=' ')
        self.current_mark = 'X'
        self.game_over = False

    def show_winner(self, mark):
        """Display a message when the player wins."""
        messagebox.showinfo("Game Over", f"Player {mark} wins!")

    def show_draw(self):
        """Display a message when the game ends in a draw."""
        messagebox.showinfo("Game Over", "It's a draw!")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
