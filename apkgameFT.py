from tkinter import *
from tkinter import messagebox as mb
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

datUser = 'admin'
datPassword = '12345'

class DemoLogin:
    def __init__(self, induk, judul):
        self.induk = induk
 
        self.induk.title(judul)
        self.induk.protocol("WM_DELETE_WINDOW", self.Tutup)
        self.induk.resizable(False, False)
 
        self.aturKomponen()
 
        self.entUser.focus_set()
 
    def aturKomponen(self):
        # atur frame utama
        frameUtama = Frame(self.induk, bd=10)
        frameUtama.pack(fill=BOTH, expand=YES)
 
        # atur frame data
        frData = Frame(frameUtama, bd=5)
        frData.pack(fill=BOTH, expand=YES)
 
        # atur input username
        Label(frData, text='nama pengguna:').grid(row=0, column=0, sticky=W)
        self.entUser = Entry(frData)
        self.entUser.grid(row=0, column=1)
 
        # atur input password
        Label(frData, text='kata kunci:').grid(row=1, column=0, sticky=W)
        self.entPass = Entry(frData, show='*')
        self.entPass.grid(row=1, column=1)
 
        # atur cek --> perlihatkan kata kunci
        self.cek = IntVar() 
 
        self.cbShowPass = Checkbutton(frData, text='lihat kata kunci',
        variable=self.cek, command=self.lihatPassword)
        self.cbShowPass.grid(row=2, column=1, sticky=E)
 
        # atur frame tombol
        frTombol = Frame(frameUtama, bd=5)
        frTombol.pack(fill=BOTH, expand=YES)
 
        # atur tombol login
        self.btnLogin = Button(frTombol, text='Login', command=self.prosesLogin)
        self.btnLogin.pack(side=LEFT, fill=BOTH, expand=YES)
 
        self.btnBatal = Button(frTombol, text='Batal', command=self.Tutup)
        self.btnBatal.pack(side=LEFT, fill=BOTH, expand=YES)
 
    def prosesLogin(self, event=None):
        # ambil data input dari pengguna
        nmUser = self.entUser.get()
        passUser = self.entPass.get()
 
        # logika pemrograman
        if nmUser=='':
            mb.showwarning('Pesan Salah', 'Nama User tidak boleh kosong!', 
parent=self.induk)
            self.entUser.focus_set()
        elif passUser=='':
            mb.showwarning('Pesan Salah', 'Kata Kunci tidak boleh kosong!', 
parent=self.induk)
            self.entPass.focus_set()
        elif (nmUser==datUser) and (passUser==datPassword):
            mb.showinfo("Login", "goodluck", parent=self.induk)
            self.Tutup()
        else:
            mb.showwarning('Pesan Salah', 'Nama Pengguna atau Kata Kunci SALAH!!', 
parent=self.induk)
            self.Hapus()
 
    def lihatPassword(self, event=None):
        nilaiCek = self.cek.get()
 
        if nilaiCek== 1:
            self.entPass['show'] = ''
        else:
            self.entPass['show'] = '*'
 
    def Tutup(self, event=None):
        self.induk.destroy()
 
    def Hapus(self, event=None):
        self.entUser.delete(0, END)
        self.entPass.delete(0, END)
        self.entUser.focus_set() 
 
if __name__ == '__main__':
    root = Tk()
 
    app = DemoLogin(root, ":: Demo Login Password ::")
 
    root.mainloop()

sign = 0


global board
board = [[" " for x in range(3)] for y in range(3)]




def winner(b, l):
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l))

def get_text(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	if winner(board, "X"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "Pemain ke 1 Menang")
	elif winner(board, "O"):
		gb.destroy()
		box = messagebox.showinfo("Winner", "Pemain ke 2 Menang")
	elif(isfull()):
		gb.destroy()
		box = messagebox.showinfo("Tie Game", "Draw")



def isfree(i, j):
	return board[i][j] == " "



def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag



def gameboard_pl(game_board, l1, l2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text, i, j, game_board, l1, l2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	game_board.mainloop()



def pc():
	possiblemove = []
	for i in range(len(board)):
		for j in range(len(board[i])):
			if board[i][j] == ' ':
				possiblemove.append([i, j])
	move = []
	if possiblemove == []:
		return
	else:
		for let in ['O', 'X']:
			for i in possiblemove:
				boardcopy = deepcopy(board)
				boardcopy[i[0]][i[1]] = let
				if winner(boardcopy, let):
					return i
		corner = []
		for i in possiblemove:
			if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
				corner.append(i)
		if len(corner) > 0:
			move = random.randint(0, len(corner)-1)
			return corner[move]
		edge = []
		for i in possiblemove:
			if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
				edge.append(i)
		if len(edge) > 0:
			move = random.randint(0, len(edge)-1)
			return edge[move]



def get_text_pc(i, j, gb, l1, l2):
	global sign
	if board[i][j] == ' ':
		if sign % 2 == 0:
			l1.config(state=DISABLED)
			l2.config(state=ACTIVE)
			board[i][j] = "X"
		else:
			button[i][j].config(state=ACTIVE)
			l2.config(state=DISABLED)
			l1.config(state=ACTIVE)
			board[i][j] = "O"
		sign += 1
		button[i][j].config(text=board[i][j])
	x = True
	if winner(board, "X"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Kamu Menang")
	elif winner(board, "O"):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Winner", "Musuh Menang")
	elif(isfull()):
		gb.destroy()
		x = False
		box = messagebox.showinfo("Tie Game", "Draw")
	if(x):
		if sign % 2 != 0:
			move = pc()
			button[move[0]][move[1]].config(state=DISABLED)
			get_text_pc(move[0], move[1], gb, l1, l2)



def gameboard_pc(game_board, l1, l2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	game_board.mainloop()



def withpc(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text="Computer : O",
				width=10, state=DISABLED)

	l2.grid(row=2, column=1)
	gameboard_pc(game_board, l1, l2)



def withplayer(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player 1 : X", width=10)

	l1.grid(row=1, column=1)
	l2 = Button(game_board, text="Player 2 : O",
				width=10, state=DISABLED)

	l2.grid(row=2, column=1)
	gameboard_pl(game_board, l1, l2)



def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Tic Tac Toe")
	wpc = partial(withpc, menu)
	wpl = partial(withplayer, menu)

	head = Button(menu, text="---Welcome to tic-tac-toe---",
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)

	B1 = Button(menu, text="Single Player", command=wpc,
				activeforeground='red',
				activebackground="yellow", bg="red",
				fg="yellow", width=500, font='summer', bd=5)

	B2 = Button(menu, text="Multi Player", command=wpl, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)

	B3 = Button(menu, text="Exit", command=menu.quit, activeforeground='red',
				activebackground="yellow", bg="red", fg="yellow",
				width=500, font='summer', bd=5)
	head.pack(side='top')
	B1.pack(side='top')
	B2.pack(side='top')
	B3.pack(side='top')
	menu.mainloop()



if __name__ == '__main__':
	play()
