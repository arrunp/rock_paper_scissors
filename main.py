from tkinter import *
from PIL import ImageTk, Image
import random
import play

play = play.Play()

window = Tk()
window.geometry("470x470")
window.resizable(False, False)

window.title("RPSLS Game")

rock_btn = Button(window, text="Rock", command=lambda: show_image(0))
paper_btn = Button(window, text="Paper", command=lambda: show_image(1))
scissors_btn = Button(window, text="Scissors", command=lambda: show_image(2))
lizard_btn = Button(window, text="Lizard", command=lambda: show_image(3))
spock_btn = Button(window, text="Spock", command=lambda: show_image(4))

rock_btn.place(x=25, y=370, width=90)
paper_btn.place(x=190, y=370, width=90)
scissors_btn.place(x=345, y=370, width=90)
lizard_btn.place(x=110, y=420, width=90)
spock_btn.place(x=280, y=420, width=90)

rock = ImageTk.PhotoImage(Image.open("img/rock.jpg"))
paper = ImageTk.PhotoImage(Image.open("img/paper.jpg"))
scissors = ImageTk.PhotoImage(Image.open("img/scissors.jpg"))
lizard = ImageTk.PhotoImage(Image.open("img/lizard.jpg"))
spock = ImageTk.PhotoImage(Image.open("img/spock.jpg"))

choices = [rock, paper, scissors, lizard, spock]

def show_image(move):
	Label(window, image=choices[play.player(move)], text="Your Move:", compound="bottom").grid(row=0, column=0)
	Label(window, image=choices[play.comp_choice], text="Computer Move:", compound="bottom").grid(row=0, column=1)
	play.winner(move)
	Label(window, text=str(play.player_score) + " - " + str(play.comp_score)).place(x=215, y=280)
	Label(window, text=play.result).place(x=205, y=320)

player_num = play.player_move
comp_num = play.comp_choice

window.mainloop()
