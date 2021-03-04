from tkinter import *
import random


root = Tk()
root.wm_iconbitmap("1.ico")
root.title("Guess")


#Automatic detect the value of screen width and height
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.configure(bg="white")


score1 = 0
score2 = 0
player1value = StringVar()
player2value = StringVar()
guess_num = IntVar()
guess_value = StringVar()
winner = StringVar()
winner.set("")
final_result=""



def click(event):
    global player2value
    text = event.widget.cget("text")
    if text == "C":
        player2value.set("")
    else:
        player2value.set(player2value.get() + text)



def click1(event):
    global player1value
    text = event.widget.cget("text")
    if text == "C":
        player1value.set("")
    else:
        player1value.set(player1value.get() + text)



def check():
    global winner
    global score2, score1
    guess_num = random.randint(1, 36)
    score1 = score1value.get()
    score2 = score2value.get()
    guess_value.set(guess_num)
    p1 = player1value.get()
    p2 = player2value.get()
    p1 = int(p1)
    p2 = int(p2)
    score1 = int(score1)
    score2 = int(score2)

    if p1 == p2 and p2 == guess_num and p1 == guess_num:
        winner.set("PLAYER A AND PLAYER B BOTH WIN")
        score1 +=10
        score2 +=10

    elif p1 == guess_num:
        winner.set("PLAYER A WIN")
        score1 +=10
        score2 -=1

    elif p2 == guess_num:
        winner.set("PLAYER B WIN")
        score2 +=10
        score1 -=1

    elif p1 == p2:
        if p1 in range(guess_num-5, guess_num+6):
            winner.set("PLAYER A AND PLAYER B BOTH WIN WITH A TIE WITH A CLOSE ASSUMPTION")
            score1 +=5
            score2 +=5
        else:
            winner.set("PLAYER A AND PLAYER B BOTH LOOSE")
            score1 -=1
            score2 -=1

    elif p1 in range(guess_num-5, guess_num+6) or p2 in range(guess_num-5, guess_num+6):
        if abs(p1-guess_num)<abs(p2-guess_num):
            winner.set("PLAYER A WIN WITH A CLOSE ASSUMPTION")
            score1 +=5
            score2 -=1
        elif abs(p1-guess_num)>abs(p2-guess_num):
            winner.set("PLAYER B WIN WITH A CLOSE ASSUMPTION")
            score2 +=5
            score1 -=1
        else:
            winner.set("PLAYER A AND PLAYER B BOTH WIN WITH A TIE WITH A CLOSE ASSUMPTION")
            score1 +=5
            score2 +=5

    else:
        winner.set("PLAYER A AND PLAYER B BOTH LOOSE")
        score1 -=1
        score2 -=1

    if score1 < 0:
        score1 = 0
    if score2 < 0:
        score2 = 0

    score1value.set(score1)
    score2value.set(score2)
    
def result():
    global final_result
    result = final_result.get()
    score1 = score1value.get()
    score2 = score2value.get()
    score1 = int(score1)
    score2 = int(score2)

    if score1>score2:
        result="PLAYER A WIN"
    elif score1<score2:
        result="PLAYER B WIN"
    else:
        result="TIE"

    final_result.set(result)

#Sceen size of window
root.maxsize(width, height)
root.minsize(width, height)


#frame1 title of the game
frame1 = Frame(root)
frame1.pack()
title = Label(frame1, text="NUMBER GUESSING GAME", font="Algerian 40 bold underline")
title.pack()



#frame4 for the guess (Number guessed by the computer between 0 - 10)
frame4 =Frame(root)
comp = Label(frame4, text=" GUESS ", font="papyrus 15 bold")
comp.pack()
guess_value.set("?")
comp1 = Entry(frame4, text=guess_value, font="papyrus 45 bold", justify='center')
comp1.pack()
frame4.pack(pady=20)



#Display the winner text from the check function
winner.set("------------------------------")
screen = Entry(root, text=winner, font="papyrus 13 bold", relief=SUNKEN, justify='center').pack(fill=X,padx=170)



#Display Final result with the comparision of score between Player A score and Player B score
final_result = StringVar()
final_result.set("")
final=Entry(root,text=final_result, font="papyrus 30 bold", relief=SUNKEN, justify='center').pack(pady=10)



#Display Score of Player A
frame2 = Frame(root)
score = Label(frame2, text="SCORE : ", font="papyrus 15 bold")
score1value = StringVar()
score1value.set("0")
scoreentry = Entry(frame2, textvariable=score1value, font="papyrus 15 bold")
score.pack()
scoreentry.pack()
player1 = Label(frame2, text="PLAYER A", font="papyrus 15 bold")
player1.pack(padx=10)
player1entry = Entry(frame2, textvariable=player1value, font="papyrus 15 bold")
player1entry.pack(pady=5)


button = Button(frame2, text="0", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="1", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="2", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="3", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="4", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="5", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="6", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="7", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="8", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="9", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
button = Button(frame2, text="C", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click1)
frame2.pack(side=LEFT, anchor='nw',padx=10)



#Display Score of Player B
frame3 = Frame(root)
score = Label(frame3, text="SCORE : ", font="papyrus 15 bold")
score2value = StringVar()
score2value.set("0")
scoreentry = Entry(frame3, textvariable=score2value, font="papyrus 15 bold")
score.pack()
scoreentry.pack()
player2 = Label(frame3, text="PLAYER B", font="papyrus 15 bold")
player2.pack(padx=10)
player2entry = Entry(frame3, textvariable=player2value, font="papyrus 15 bold")
player2entry.pack(pady=5)


button = Button(frame3, text="0", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="1", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="2", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="3", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="4", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="5", font="papyrus 15 bold")
button.pack(side=LEFT,padx=3)
button.bind("<Button-1>", click)
buttonframe = Frame(frame3)
button = Button(frame3, text="6", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="7", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="8", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="9", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
button = Button(frame3, text="C", font="papyrus 15 bold")
button.pack(side=LEFT, padx=3)
button.bind("<Button-1>", click)
frame3.pack(side=RIGHT, anchor='ne', padx=10)



#Start Button
frame5 = Frame(root)
Button(frame5, text="Start", font="papyrus 15 bold", command=check).pack()
Button(frame5, text="Result", font="papyrus 15 bold", command=result).pack(pady=10)
frame5.pack(pady=100)


root.mainloop()
