from tkinter import *
import tkinter as tk


def button1command():
  adjective = input("Enter an adjective: ")
  adjective2 = input("Enter another adjective: ")
  bone = input("Enter a bone name: ")
  bone2 = input("\nEnter another bone name: ")
  print(f"\n\nadjective.get() {adjective2} skin. Every morning I break my {bone}, and every afternoon I break my {bone2}, at night I lie awake in agony until my heart attacks put me to sleep. \n\n\nSpongebob Squarepants: Season 3 Episode 12")

def button2command():
  food = input("Enter a food: ")
  item = input("Enter a weird item: ")
  print(f"\nYou little- you sack of {food}, I dumped you because you're dragging around a 35 year old {item}!\n\n\nArcher: Season 1 Episode 1")

def button3command():
  condiment1 = input("Enter a type of condiment: ")
  condiment2 = input("Enter another type of condiment: ")
  condiment3 = input("Enter another type of condiment: ")
  print(f"\nLast night I dreamed I was a bottle of {condiment1}. And you were {condiment2}. Which is weird, because usually you're {condiment3} in my dreams. Why do you suppose that is? \n\n\nChowder: Season 1 Episode 1")

def button4command():
  mc = input("Enter a mythical creature (plural pls): ")
  bp = input("Enter a body part: ")
  mcn = input("Enter the same mythical creature (not plural pls): ")
  print(f"Beware the teeth of the deadly {mc}. They'll bite your {bp} when you're all alone. And they'll drag you back to their little {mcn} home. Where they'll boil you for stew till you're nothing but bone!\n\nCamp Lazlo: Season 2 Episode 12")

def button5command():
  noun = input("Enter a noun or a name: ")
  c = input("Enter an academic class:  ")
  print(f"Look, {noun}, can you have your meltdown somewhere else? I've got a {c} report due tomorrow on the history of {c}... and you're kind of distracting me. \n\nThe Grim Adventures of Bill And Mandy")

def button6command():
  name = input("Enter a name: ")
  club = input("Enter a type of recreational club: ")
  new_name = input("Enter a new name: ")
  mc = input("Enter a mythical creture: ")
  pn = input("Enter a pronoun (he/she/they): ")
  print(f"\n{name}, you do not want that flu bug. I had it and it gave me weird fever dreams. I dreamt I was in a {club} club with my cousin {new_name}, but {pn} was a {mc}.\n\nBob's Burgers Season 7 Episode 1")

root=tk.Tk()
root.title("J's MadLibs") 
root.config(bg = 'dark green')
root.geometry("875x875")

label1 = tk.Label(root, text = "Select A MadLib Story To Begin", font = '35')
label1.pack()

button1=tk.Button(root, text ="Injured Fish", font = 'Aerial 15 bold', command = button1command)
button1.pack()
button1.place(x=30, y=50)

button2=tk.Button(root, text ="Lana's Fed Up", font = 'Aerial 15 bold', command = button2command)
button2.pack()
button2.place(x=30, y=110)

button3=tk.Button(root, text ="Chowder's Peculiar Dream", font = 'Aerial 15 bold', command = button3command)
button3.pack()
button3.place(x=30, y=360)

button4=tk.Button(root, text ="Slinkman's Warning", font = 'Aerial 15 bold', command = button4command)
button4.pack()
button4.place(x=30, y=240)

button5=tk.Button(root, text ="Mandy's Intrusion", font = 'Aerial 15 bold', command = button5command)
button5.pack()
button5.place(x=30, y=175)

button6=tk.Button(root, text ="Down With The Sickness", font = 'Aerial 15 bold', command = button6command)
button6.pack()
button6.place(x=30, y=300)

root.mainloop()