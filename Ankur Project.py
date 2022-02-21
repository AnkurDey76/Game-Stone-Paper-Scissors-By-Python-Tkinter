from ast import Lambda
from distutils.command.config import config
from pickletools import int4
from select import select
from tkinter import *
from turtle import update
from PIL import Image, ImageTk
from random import randint
window= Tk()
window.title("Game Stone Paper Scissors By Ankur")
window.configure(background="grey")

image_rock1= ImageTk.PhotoImage(Image.open("Rock 1.png"))
image_paper1= ImageTk.PhotoImage(Image.open("Paper 1.png"))
image_scissor1= ImageTk.PhotoImage(Image.open("Scissor 1.png"))
image_rock2= ImageTk.PhotoImage(Image.open("Rock 2.png"))
image_paper2= ImageTk.PhotoImage(Image.open("Paper 2.png"))
image_scissor2= ImageTk.PhotoImage(Image.open("Scissor 2.png"))

label_player= Label(window,image=image_scissor1)
label_computer= Label(window,image= image_scissor2)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=4)

computer_score= Label(window,text=0,font=("arial", 60, "bold"), fg= "red")
player_score= Label(window,text=0,font=("arial", 60, "bold"), fg= "red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=3)




def updateMessage(a):
    final_message['text']=a

def computer_update():
    final= int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)

def player_update():
    final= int(player_score['text'])
    final+=1
    player_score["text"]=str(final)


def winner_check(p, c):
    if p==c:
        updateMessage("It's a tie!")
    elif p=="rock":
         if c=="paper":
          updateMessage("Computer Wins!")
          computer_update()
         else:
           updateMessage("You Win!")
           player_update()

    elif p=="paper":
         if c=="scissor":
          updateMessage("Computer Wins!")
          computer_update()
         else:
           updateMessage("You Win!")
           player_update()

    elif p=="scissor":
         if c=="rock":
          updateMessage("Computer Wins!")
          computer_update()
         else:
           updateMessage("You Win!")
           player_update()

    else:
        pass



to_select= ["rock", "paper", "scissor"]

def choice_update(a):
    choice_computer= to_select[randint(0, 2)]
    if choice_computer=="rock":
       label_computer.configure(image= image_rock2)

    elif choice_computer=="paper":
       label_computer.configure(image= image_paper2)
    
    else:
        label_computer.configure(image= image_scissor2)



    if a=="rock":
       label_player.configure(image= image_rock1)

    elif a=="paper":
       label_player.configure(image= image_paper1)
    
    else:
        label_player.configure(image= image_scissor1)


    winner_check(a, choice_computer)







def msg_updation(a):
    final_message['text']=a

def computer_update():
    final= int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)

def player_update():
    final= int(player_score['text'])
    final+=1
    player_score["text"]=str(final)



final_message= Label(window,text=0,font=("comic sans ms", 40, "bold"),bg="blue", fg= "white")
final_message.grid(row=3,column=2)

player_indicator= Label(window,font=("arial italic", 30, "bold"),text="YOU",fg="blue",bg= "orange")
computer_indicator= Label(window,font=("arial italic", 30, "bold"),text="COMPUTER",fg="blue",bg= "orange")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)



button_rock= Button(window, width=16, height=3,text="STONE", font=("Helvetica", 20, "bold"),bg="brown",fg="yellow", command=lambda: choice_update("rock")).grid(row=2,column=1)

button_paper= Button(window, width=16, height=3,text="PAPER",font=("arial", 20, "bold"), bg= "white", fg= "green", command=lambda: choice_update("paper")).grid(row=2, column=2)

button_scissor= Button(window, width=16, height=3,text="SCISSOR",font=("arial", 20, "bold"), bg= "yellow", fg= "red", command=lambda: choice_update("scissor")).grid(row=2, column=3)

window.mainloop()