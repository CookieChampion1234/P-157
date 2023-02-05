from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("Pokemon card game")
root.geometry("900x900")
root.configure(background = "gold")

abra = ImageTk.PhotoImage(Image.open ("abra.jpg"))
meowth = ImageTk.PhotoImage(Image.open ("meowth.jpg"))
ivysaur = ImageTk.PhotoImage(Image.open ("Iyvasour.jpg"))
paras = ImageTk.PhotoImage(Image.open ("paras.jpg"))
pikachu = ImageTk.PhotoImage(Image.open ("pikachu.jpg"))
jigglypuff = ImageTk.PhotoImage(Image.open ("jigglypuff.jpg"))
kadabra = ImageTk.PhotoImage(Image.open ("kadabra.jpg"))
charmander = ImageTk.PhotoImage(Image.open ("charmender.jpg"))
bulbasaur = ImageTk.PhotoImage(Image.open ("bulbasour.jpg"))
rattata = ImageTk.PhotoImage(Image.open ("ratata.jpg"))
squirtle = ImageTk.PhotoImage(Image.open ("squirtle.jpg"))
nidoking = ImageTk.PhotoImage(Image.open ("nidoking.jpg"))
persian = ImageTk.PhotoImage(Image.open ("persion.jpg"))

player1 = Label(root, text = "Player 1", bg = "royal blue", fg = "white")
player1.place(relx = 0.1, rely = 0.3, anchor= CENTER)

player2 = Label(root, text = "Player 2", bg = "royal blue", fg = "white")
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)

Player1_score_label = Label(root, bg = "royal blue", fg = "white")
Player1_score_label.place(relx = 0.1, rely = 0.4, anchor = CENTER)

Player2_score_label = Label(root, bg = "royal blue", fg = "white")
Player2_score_label.place(relx = 0.9, rely = 0.4, anchor = CENTER)

random_pokecard_label = Label(root, fg = "white")
random_pokecard_label.place(relx = 0.5, rely = 0.5, anchor = CENTER)


Pokemon = [abra, bulbasaur , charmander , ivysaur , jigglypuff , kadabra , meowth , nidoking , paras , persian , pikachu , rattata , squirtle ]
power = ["30","60","50","100","70","70","60","90","40","70","200","40","50"] 



def player1():
   player1_score = ""
   randomNumber = random.randint(0,12)
   random_pokemon = Pokemon[randomNumber]
   random_pokecard_label["image"] = random_pokemon
   print(power[randomNumber])
   score = player1_score + power[randomNumber]
   player1_score = score
   Player1_score_label["text"] = player1_score
   
   
   
def player2():
   player2_score = ""
   randomNumber2 = random.randint(0,12)
   random_pokemon2 = Pokemon[randomNumber2]
   random_pokecard_label["image"] = random_pokemon2
   print(power[randomNumber2])
   score2 = player2_score + power[randomNumber2]
   player2_score = score2
   Player2_score_label["text"] = player2_score


btn_player1 = Button(root, text = "player1", bg = "royal blue", fg = "white", command=player1)
btn_player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)

btn_player2 = Button(root, text = "player2", bg = "royal blue", fg = "white", command=player2)
btn_player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)


root.mainloop()


