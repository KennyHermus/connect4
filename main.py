import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color.upper()


class Piece:
    window = tk.Tk()
    piece_width = window.winfo_screenwidth() // 7
    piece_height = window.winfo_screenheight() // 6

    def __init__(self):
        self.color = True

    def getWindow(self):
        return self.window

    def genRed(self):
        red_path = "red.png"
        red = ImageTk.PhotoImage(Image.open(red_path).resize((self.piece_width, self.piece_height), Image.ANTIALIAS))
        red_piece = tk.Label(self.window, image=red, width=self.piece_width, height=self.piece_height)
        red_piece.img = red
        red_piece.place(x=int(self.window.winfo_screenwidth() / 2.4), y=int(self.window.winfo_screenheight() // 1.2))
        # self.graphic.tkraise(red_piece)
        return red_piece

    # create yellow piece
    def genYel(self):
        yellow_path = "yellow.png"
        yellow = ImageTk.PhotoImage(
            Image.open(yellow_path).resize((self.piece_width, self.piece_height), Image.ANTIALIAS))
        yellow_piece = tk.Label(self.window, image=yellow, width=self.piece_width, height=self.piece_height)
        yellow_piece.img = yellow
        yellow_piece.place(x=int(self.window.winfo_screenwidth() / 2.4), y=int(self.window.winfo_screenheight() // 1.2))
        # self.graphic.tkraise(yellow_piece)
        return yellow_piece

    def genEmpty(self):
        empty_path = "empty.png"
        empty = ImageTk.PhotoImage(Image.open(empty_path).resize((self.piece_width, self.piece_height), Image.ANTIALIAS))
        empty_piece = tk.Label(self.window, image=empty, width=self.piece_width, height=self.piece_height)
        empty_piece.img = empty
        empty_piece.place(x=int(self.window.winfo_screenwidth() / 2.4), y=int(self.window.winfo_screenheight() // 1.2))
        return empty_piece

    @property
    def getWidth(self):
        return self.piece_width

    @property
    def getHeight(self):
        return self.piece_height


class Board:
    def __init__(self, width, height):
        self.board = []
        self.width = width
        self.height = height

    def reset_board(self):
        for i in range(self.height):
            self.board.append([])
            for piece in range(self.width):
                self.board[i].append("O")

    def display_board(self):
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    @property
    def get_board(self):
        return self.board

    @property
    def get_width(self):
        return self.width

    @property
    def get_height(self):
        return self.height


class GraphicBoard(Board, Piece):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.graphic = []
        self.bgrd = None

    # create board
    def makeBoard(self):
        '''
        board_path = "~/Documents/c_four_board.png"
        img = ImageTk.PhotoImage(Image.open(board_path).resize(
            (super().getWindow().winfo_screenwidth(), super().getWindow().winfo_screenheight()), Image.ANTIALIAS))
        self.graphic = tk.Label(super().getWindow(), image=img, width=super().getWindow().winfo_screenwidth(),
                                height=super().getWindow().winfo_screenheight())
        self.graphic.image = img  # this feels redundant but the image didn't show up without it in my app
        self.graphic.pack()
        '''
        for row in range(self.height):
            self.graphic.append([])
            for col in range(self.width):
                piece = Piece()
                field = piece.genEmpty()
                self.graphic[row].append(field)

        for row in range(self.height):
            for col, piece in enumerate(self.graphic[row]):
                piece.place(x=1+((col) * super().getWidth),
                      y= -5 + super().getWindow().winfo_screenheight() - (6 - row) * super().getHeight)
                #piece.tkraise(self.getBgrd())

    def setBgrd(self):
        bgrd_path = "background.png"
        img = ImageTk.PhotoImage(Image.open(bgrd_path).resize(
            (super().getWindow().winfo_screenwidth(), super().getWindow().winfo_screenheight()), Image.ANTIALIAS))
        self.bgrd = tk.Label(super().getWindow(), image=img, width=super().getWindow().winfo_screenwidth(),
                                height=super().getWindow().winfo_screenheight())
        self.bgrd.image = img  # this feels redundant but the image didn't show up without it in my app
        self.bgrd.pack()

    def getBgrd(self):
        return self.bgrd

    def getGraphic(self):
        return self.graphic


class ConnectFour(GraphicBoard):
    def __init__(self):
        super().__init__(7, 6)
        self.gwindow = super().getWindow()
        self.turn = 1

    def get_players(self):
        name1 = input("Player 1, Enter Your Name: ")
        name2 = input("Player 2, Enter Your Name: ")
        color1 = "Red"
        color2 = "Yellow"
        self.player1 = Player(name1, color1)
        self.player2 = Player(name2, color2)

    @property
    def whose_turn(self):
        if self.turn % 2 == 1:
            return self.player1
        return self.player2

    def show_graphic(self, row, col):
        if super().get_board[row - 1][col - 1] == "R":
            piece = Piece()
            red = piece.genRed()
            red.place(x=((col - 1) * super().getWidth),
                      y=-5 + super().getWindow().winfo_screenheight() - (7 - row) * super().getHeight)
            #red.tkraise(super().getGraphic()[row-1][col-1])
        elif super().get_board[row - 1][col - 1] == "Y":
            piece = Piece()
            yel = piece.genYel()
            yel.place(x=((col - 1) * super().getWidth),
                      y=-5 + super().getWindow().winfo_screenheight() - (7 - row) * super().getHeight)
            #yel.tkraise(super().getGraphic()[row-1][col-1])

    def make_move(self, col):
        for row in range(super().get_height - 1):
            if super().get_board[row][col - 1] == "O" and super().get_board[row + 1][col - 1] != "O":
                super().get_board[row][col - 1] = self.whose_turn.color[0]
                self.turn += 1
                self.show_graphic(row + 1, col)
                return
        super().get_board[super().get_height - 1][col - 1] = self.whose_turn.color[0]
        self.show_graphic(super().get_height, col)
        self.turn += 1

    def get_col(self, event):
        col = event.x // super().piece_width + 1
        return self.make_move(col)

    def get_event(self, event):
        return self.get_col(event)

    def check_diags(self):
        for row in range(super().get_height - 1, super().get_height - 4, -1):
            for col in range(super().get_width - 3):
                if super().get_board[row][col] != "O" and super().get_board[row][col] == super().get_board[row - 1][
                    col + 1] and super().get_board[row - 1][col + 1] == super().get_board[row - 2][col + 2] and \
                        super().get_board[row - 2][col + 2] == super().get_board[row - 3][col + 3]:
                    return True
        for row in range(super().get_height - 1, super().get_height - 4, -1):
            for col in range(super().get_width - 1, super().get_width - 5, -1):
                if super().get_board[row][col] != "O" and super().get_board[row][col] == super().get_board[row - 1][
                    col - 1] and super().get_board[row - 1][col - 1] == super().get_board[row - 2][col - 2] and \
                        super().get_board[row - 2][col - 2] == super().get_board[row - 3][col - 3]:
                    return True
        return False

    def check_horiz(self):
        for row in range(super().get_height):
            for col in range(super().get_width - 3):
                if super().get_board[row][col] != "O" and super().get_board[row][col] == super().get_board[row][
                    col + 1] and super().get_board[row][int(col) + 1] == super().get_board[row][int(col) + 2] and \
                        super().get_board[row][int(col) + 2] == super().get_board[row][int(col) + 3]:
                    return True
        return False

    def check_vert(self):
        for col in range(super().get_width):
            for row in range(super().get_height - 3):
                if super().get_board[row][col] != "O" and super().get_board[row][col] == super().get_board[row + 1][
                    col] and super().get_board[row + 1][col] == super().get_board[row + 2][col] and \
                        super().get_board[row + 2][col] == super().get_board[row + 3][col]:
                    return True
        return False

    def gameOver(self):
        return self.check_horiz() or self.check_vert() or self.check_diags()

    def play_game(self):
        super().reset_board()
        self.gwindow.title("Connect 4")
        self.get_players()
        super().setBgrd()
        lbl = tk.Label(text=f'Turn {self.turn}: {self.whose_turn.name}, make your move.', font=("Arial", 25))
        lbl.tkraise(super().getBgrd())
        lbl.pack()
        super().makeBoard()
        running = True
        while not self.gameOver() and running:
            current_turn = self.turn
            self.gwindow.bind("<Button-1>", self.get_event)
            lbl["text"] = f'Turn {self.turn}: {self.whose_turn.name}, make your move.'
            while (not self.gameOver()) and (current_turn == self.turn) and running:
                self.gwindow.update_idletasks()
                self.gwindow.update()
        self.turn += 1
        print(f'{self.whose_turn.name} wins!')


c = ConnectFour()
c.play_game()
