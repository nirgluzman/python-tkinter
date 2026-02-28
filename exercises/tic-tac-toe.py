import tkinter as tk

BG_COLOR = "#4E0505"


class App(tk.Tk):
    def __init__(self, title, size):
        super().__init__()

        # Set the title of the main window
        self.title(title)

        # Set the background color of the main window
        self.config(bg=BG_COLOR)

        # Set the size of the main window and prevent resizing
        self.geometry(f"{size[0]}x{size[1]}")
        self.resizable(False, False)

        # Create the menu bar
        Menu(self)

        # Create the game board (initially None)
        self.game = None

        # Main event loop
        self.mainloop()


class Menu(tk.Menu):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Attach menu to parent window
        parent.configure(menu=self)

        # Game submenu
        game_menu = tk.Menu(master=parent, tearoff=False)
        game_menu.add_command(label="New", command=lambda: self.start_new_game(parent))
        game_menu.add_command(label="Exit", command=parent.destroy)
        self.add_cascade(label="Game", menu=game_menu)

        # Help submenu
        help_menu = tk.Menu(master=parent, tearoff=False)
        self.add_cascade(label="Help", menu=help_menu)

    def start_new_game(self, parent):
        # Destroy existing game and create a new one
        if parent.game:
            parent.game.destroy()
        parent.game = Game(parent)


class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(master=parent)

        # Set the background color of the game frame
        self.config(bg=BG_COLOR)

        # Current player's turn - alternates between "X" and "O"
        self.current_player = "X"

        # Flag to track if the game has ended (winner found or board full)
        self.game_over = False

        # 3x3 game board to track the state of each cell (empty string means unoccupied)
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Winner label
        self.winner_label = tk.Label(
            self, text="", font=("Arial", 32), bg=BG_COLOR, fg="white"
        )

        # Create 4x3 grid (row 0 for label, rows 1-3 for game)
        for i in range(3):
            self.columnconfigure(
                i,
                weight=1,
                uniform="equal_cells",
                minsize=150,  # minsize > font size + (Padding * 2) + Border
            )

        self.rowconfigure(0, weight=0)  # Label row - doesn't expand on resize
        for i in range(1, 4):
            self.rowconfigure(i, weight=1, uniform="equal_cells", minsize=150)

        self.winner_label.grid(row=0, column=0, columnspan=3, pady=10)

        # Place 9 buttons in 3x3 grid (starting at row 1)
        for row in range(3):
            for col in range(3):
                button = tk.Button(
                    master=self, text="", font=("Arial", 100), relief="flat"
                )
                button.grid(row=row + 1, column=col, padx=5, pady=5, sticky="nsew")
                button.bind(
                    "<ButtonPress-1>",
                    lambda event, row=row, col=col: self.press(event, row, col),
                )

        self.pack(expand=True, fill="both", padx=20, pady=20)

    def press(self, event, row, col):
        # Ignore clicks if game is over or cell is already filled
        if self.game_over or self.board[row][col] != "":
            return

        color = "red" if self.current_player == "X" else "blue"

        clicked_button = event.widget
        self.update_button(clicked_button, self.current_player, color)
        self.board[row][col] = self.current_player

        if self.check_winner():
            self.game_over = True
            self.winner_label.config(text=f"{self.current_player} wins !!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"

    def update_button(self, button, text, color):
        button.config(text=text, fg=color)

    def check_winner(self):
        # Check if there is a winner by examining all possible winning combinations:
        # horizontal rows, vertical columns, and both diagonal lines
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False


def main():
    App("Tic Tac Toe", (600, 600))


main()
