from tkinter import *
import random
import tkinter.messagebox

root = Tk()
root.title("Number Guessing Game")
root.geometry("500x300")

def greet():
    name = entry1.get()
    tkinter.messagebox.showinfo("My Name", "Well, "+name+", I am thinking of a number between 1 and 20.")

number = random.randint(1,20)

def guessButton():
    guess = int(entry2.get())
    if guess > number:
        tkinter.messagebox.showinfo("higher", "Your guess is too high!")
    elif guess < number:
        tkinter.messagebox.showinfo("lower", "Your guess is too low!")
    elif guess == number:
        tkinter.messagebox.showinfo("correct", "You've guessed correctly!")


label1 = Label(root, text="Welcome to our game!")
label1.pack()
 
label2 = Label(root, text="Enter your name:")
label2.place(x=50,y=50)

entry1= Entry(root)
entry1.place(x=50, y=70)

button1 = Button(root, text="OK", command=greet)
button1.place(x=200, y=65)

label3 = Label(root, text="Guess a number:")
label3.place(x=50, y=120)

entry2 = Entry(root)
entry2.place(x=150, y=121)

button2 = Button(root, text="Guess", command= guessButton)
button2.place(x=290, y=116)




root.mainloop()