from tkinter import *
from PIL import Image, ImageTk

#Second Button in MadLib Window - Injured Fish
def first_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, adj, adjs, bone, abone):
        text = f'''I was born with {adj} bones and {adjs} skin. Every morning I break my {bone} and every afternoon I break my {abone}, at night I lie awake in agony until my heart attacks put me to sleep. \n\n\n Spongebob Squarepants: Season 3 Episode 12.'''
        
        tl.geometry(newGeometry='600x500')
        
        Label(tl, text= 'Your Story:', font=("Comic Sans MS", 13, 'bold'), background='LightBlue', wraplength=tl.winfo_width()).place(x=250, y=300)
        Label(tl, text=text, font=("Comic Sans MS", 13), background='lightblue', wraplength=tl.winfo_width()).place(x=15, y=330)
        
    #toplevel widget first madlib
    ml1_wn = Toplevel(win,bg='LightBlue')
    ml1_wn.title("Injured Fish")
    ml1_wn.geometry('600x500')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)
    
    #creating labels
    Label(ml1_wn, text='Injured Fish MadLib', font=("Comic Sans MS", 20, 'bold'), bg='LightBlue').place(x=150, y=0)
    
    Label(ml1_wn, text='Adjective:', font=("Comic Sans MS", 15), bg='LightBlue').place(x=100, y=75)
    Label(ml1_wn, text='Another Adjective:', font=("Comic Sans MS", 15), bg='LightBlue').place(x=100, y=115)
    Label(ml1_wn, text='Bone:', font=("Comic Sans MS", 15), bg='LightBlue').place(x=100, y=155)
    Label(ml1_wn, text='Another Bone:', font=("Comic Sans MS", 15), bg='LightBlue').place(x=100, y=195)

    #text input
    adj_entry = Entry(ml1_wn, width=17)
    adj_entry.place(x=390, y=75)
    adjs_entry = Entry(ml1_wn, width=17)
    adjs_entry.place(x=390, y=110)
    
    #option menu
    bones = ['skull','spine','clavicle','wrist','pelvis','femur','tarsal']
    abones = ['skull','spine','clavicle','wrist','pelvis','femur','tarsal']
    
    bone_opt = StringVar(ml1_wn)
    bone_opt.set(bones[0])
    OptionMenu(ml1_wn, bone_opt, *bones).place(x=410, y= 155)
    
    abone_opt = StringVar(ml1_wn)
    abone_opt.set(abones[0])
    OptionMenu(ml1_wn, abone_opt, *abones).place(x=410, y= 195)
    
    #submit button
    submit_btn = Button(ml1_wn, text= "Submit", background= "pink", font=('Comic Sans MS', 12), command=lambda:finish_madlib(ml1_wn, adj_entry.get(), adjs_entry.get(), bone_opt.get(), abone_opt.get()))
    submit_btn.place(x=260, y=250)
    
    ml1_wn.mainloop()
    
    
#First Button in MadLib Window - Archer!!!
def second_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, food, item):
        text = f'''You little- you sack of {food}, I dumped you because you're dragging around a 35 year old {item}!\n\n\nArcher: Season 1 Episode 1'''
        
        tl.geometry(newGeometry='550x400')
        
        Label(tl, text='Your Story:', font=("Comic Sans MS", 13, "bold"), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=210, y=190)
        Label(tl, text=text, font=("Comic Sans MS", 13), wraplength=tl.winfo_width(), bg='RoyalBlue2').place(x=20, y=240)
        
    #top level widget 
    ml2_wn = Toplevel(win, bg='RoyalBlue2')
    ml2_wn.title("Archer!!!")
    ml2_wn.geometry('550x400')
    ml2_wn.resizable(False, False)
    ml2_wn.iconphoto(False, logo)
    
    #create labels
    Label(ml2_wn, text='Archer!!!', font=("Comic Sans MS", 17, 'bold'), bg='RoyalBlue2').place(x=220, y=0)

    Label(ml2_wn, text='Food:', font=("Comic Sans MS", 15), bg='RoyalBlue2').place(x=100, y=50)
    Label(ml2_wn, text='Weird Item:', font=("Comic Sans MS", 15), bg='RoyalBlue2').place(x=100, y=85)
    
    # Creating the text input boxes to enter the data in for the user
    foods_entry = Entry(ml2_wn, width=19)
    foods_entry.place(x=275, y=50)

    item_entry = Entry(ml2_wn, width=19)
    item_entry.place(x=275, y=85)
    
    #submit btn
    submit_btn = Button(ml2_wn, text="Submit", background="SteelBlue", font=('Times', 12), command=lambda: finish_madlib(ml2_wn, foods_entry.get(), item_entry.get()))
    submit_btn.place(x=230, y=150)

    ml2_wn.mainloop()
    

# Sixth Button in MadLib Window - Chowder's Peculiar Dream     
def third_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, condiment1, condiment2, condiment3):
        text = f'''Last night I dreamed I was a bottle of {condiment1}. And you were {condiment2}. Which is weird, because usually you're {condiment3} in my dreams. Why do you suppose that is? \n\n\nChowder: Season 1 Episode 1 '''
        
        tl.geometry(newGeometry='550x500')
        
        Label(tl, text='Your Story:', font=("Comic Sans MS", 13, "bold"), wraplength=tl.winfo_width(), bg='peachpuff2').place(x=220, y=260)
        Label(tl, text=text, font=("Comic Sans MS", 13), wraplength=tl.winfo_width(), bg='peachpuff2').place(x=15, y=320)
        
    # Creating the top level widget e
    ml3_wn = Toplevel(win, bg='purple')
    ml3_wn.title("Chowders Peculiar Dream ")
    ml3_wn.geometry('550x500')
    ml3_wn.resizable(False, False)
    ml3_wn.iconphoto(False, logo)
    
    # Creating the labels 
    Label(ml3_wn, text='Chowders Peculiar Dream', font=("Comic Sans MS", 17, 'bold'), bg='peachpuff2').place(x=140, y=0)

    Label(ml3_wn, text='First condiment:', font=("Comic Sans MS", 15), bg='peachpuff2').place(x=50, y=50)
    Label(ml3_wn, text='Second condiment:', font=("Comic Sans MS", 15), bg='peachpuff2').place(x=50, y=100)
    Label(ml3_wn, text='Third condiment:', font=("Comic Sans MS", 15), bg='peachpuff2').place(x=50, y=150)
    
    condiments1_entry = Entry(ml3_wn, width=19)
    condiments1_entry.place(x=345, y=55)

    condiments2_entry = Entry(ml3_wn, width=19)
    condiments2_entry.place(x=345, y=107)

    condiments3_entry = Entry(ml3_wn, width=19)
    condiments3_entry.place(x=345, y=160)
    
    # Creating a 'Submit' button 
    submit_btn = Button(ml3_wn, text="Submit", background="peachpuff2", font=('Comic Sans MS', 12), command=lambda: finish_madlib(ml3_wn, condiments1_entry.get(), condiments2_entry.get(), condiments3_entry.get()))
    submit_btn.place(x=240, y=210)

    ml3_wn.mainloop()
    

#Slinkman's Warning
def fourth_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, mc, bp, mcn):
        
        text = f'''Beware the teeth of the deadly {mc}. They'll bite your {bp} when you're all alone. And they'll drag you back to their little {mcn} home. Where they'll boil you for stew till you're nothing but bone!\n\nCamp Lazlo: Season 2 Episode 12'''

        tl.geometry(newGeometry='600x500')
        
        Label(tl, text='Your Story:', font=("Comic Sans MS", 13, 'bold'), background='aquamarine4', wraplength=tl.winfo_width()).place(x=255, y=320)
        Label(tl, text=text, font=("Comic Sans MS", 13), background='aquamarine4', wraplength=tl.winfo_width()).place(x=0, y=360)
        
        
    # Creating the top level widget for the first mad lib game
    ml1_wn = Toplevel(win, bg='aquamarine4')
    ml1_wn.title("Slinkmans Warning")
    ml1_wn.geometry('600x500')
    ml1_wn.resizable(False, False)
    ml1_wn.iconphoto(False, logo)
    
    
    # Creating the labels that will display the text on the screen, with background as "Gold" and font as 20-point Helvetica
    Label(ml1_wn, text="Slinkman's Warning", font=("Comic Sans MS", 20, 'bold'), bg='aquamarine4').place(x=170, y=0)

    Label(ml1_wn, text='Mythical Creature:', font=("Comic Sans MS", 15), bg='aquamarine4').place(x=50, y=70)
    Label(ml1_wn, text='Body Part:', font=("Comic Sans MS", 15), bg='aquamarine4').place(x=50, y=130)
    Label(ml1_wn, text='Mythical Creature\n(same as above):', font=("Comic Sans MS", 15), bg='aquamarine4').place(x=50, y=190)

    #options menu
    mc = ['leprechauns', 'elves', 'fairies', 'gnomes', 'goblins', 'trolls', 'dark elves', 'unicorns']
    bp = ['ears', 'toes', 'nose', 'calves', 'back', 'neck', 'shoulders', 'wrist', 'knees', 'arms']
    mc2 = ['leprechaun', 'elf', 'fairy', 'gnome', 'goblin', 'troll', 'dark elf', 'unicorn']
    
    mcs_opt = StringVar(ml1_wn)
    mcs_opt.set(mc[0])
    OptionMenu(ml1_wn, mcs_opt, *mc).place(x=450, y=75)
    
    bps_opt = StringVar(ml1_wn)
    bps_opt.set(bp[0])
    OptionMenu(ml1_wn, bps_opt, *bp).place(x=450, y=135)
    
    mcs2_opt = StringVar(ml1_wn)
    mcs2_opt.set(mc2[0])
    OptionMenu(ml1_wn, mcs2_opt, *mc2).place(x=450, y=200)
    
    submit_btn = Button(ml1_wn, text="Submit", background="DarkOrange4", font=('Comic Sans MS', 12), command=lambda:finish_madlib(ml1_wn, mcs_opt.get(), bps_opt.get(), mcs2_opt.get()))
    submit_btn.place(x=270, y=260)
    
    ml4.mainloop()
    
    
def fifth_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, noun, subject, topic):
        text = f'''Look, {noun}, can you have your meltdown somewhere else? I've got a {subject} report due tomorrow on the history of {topic}... and you're kind of distracting me. \n\nThe Grim Adventures of Bill And Mandy.'''
        
        tl.geometry(newGeometry= '500x500')
        
        Label(tl, text='Your Story:', font=("Comic Sans MS", 13, "bold"), wraplength=tl.winfo_width(), bg='teal').place(x=200, y=290)
        
        Label(tl, text=text, font=("Comic Sans MS", 13), wraplength=tl.winfo_width(), bg='teal').place(x=10, y=330)

	# Creating the top level widget 
    ml5_wn = Toplevel(win, bg='teal')
    ml5_wn.title("Mandy's Intrusion")
    ml5_wn.geometry('500x500')
    ml5_wn.resizable(False, False)
    ml5_wn.iconphoto(False, logo)
    
    Label(ml5_wn, text= "Mandy's Intrusion", font=("Comic Sans MS", 17, 'bold'), bg='pink').place(x=145, y=0)

    Label(ml5_wn, text='Noun/Insulting Name:', font=("Comic Sans MS", 15), bg='pink').place(x=50, y=70)
    Label(ml5_wn, text='Random Subject:', font=("Comic Sans MS", 15), bg='pink').place(x=50, y=130)
    Label(ml5_wn, text='Random Topic', font=("Comic Sans MS", 15), bg='pink').place(x=50, y=190)
	
    noun_entry = Entry(ml5_wn, width=19)
    noun_entry.place(x=350, y=75)

    subject_entry = Entry(ml5_wn, width=19)
    subject_entry.place(x=350, y=135)
    
    topic_entry = Entry(ml5_wn, width=19)
    topic_entry.place(x=350, y=195)
    
    submit_btn = Button(ml5_wn, text="Submit", background="yellow", font=('Comic Sans MS', 12), command=lambda:finish_madlib(ml5_wn, noun_entry.get(), subject_entry.get(), topic_entry.get(),))
    submit_btn.place(x=220, y=235)

    ml5_wn.mainloop()


def sixth_madlib(win, logo: PhotoImage):
    def finish_madlib(tl: Toplevel, name,club, new_name, pn, mc):
        text = f'''{name}, you do not want that flu bug. I had it and it gave me weird fever dreams. I dreamt I was in a {club} club with my cousin, {new_name}, but {pn} was a {mc}.\n\nBob's Burgers Season 7 Episode 1'''
        
        tl.geometry(newGeometry= '630x575')
        
        Label(tl, text='Your Story:', font=("Comic Sans MS", 13, "bold"), wraplength=tl.winfo_width(), bg='lightgreen').place(x=250, y=370)
        Label(tl, text=text, font=("Comic Sans MS", 13), wraplength=tl.winfo_width(), bg='lightgreen').place(x=10, y=425)
    
    ml6_wn = Toplevel(win, bg='lightgreen')
    ml6_wn.title("Down With The Sickness")
    ml6_wn.geometry('630x575')
    ml6_wn.resizable(False, False)
    ml6_wn.iconphoto(False, logo)
    
    Label(ml6_wn, text='Down With The Sickness', font=("Comic Sans MS", 17, 'bold'), bg='lightgreen').place(x=170, y=0)
    
    Label(ml6_wn, text='Name:', font=("Comic Sans MS", 15), bg='lightgreen').place(x=30, y=70)
    Label(ml6_wn, text='Recreational Club/Activity:', font=("Comic Sans MS", 15), bg='lightgreen').place(x=30, y=110)
    Label(ml6_wn, text='New Name:', font=("Comic Sans MS", 15), bg='lightgreen').place(x=30, y=150)
    Label(ml6_wn, text='Pronoun:', font=("Comic Sans MS", 15), bg='lightgreen').place(x=30, y=190)
    Label(ml6_wn, text="Mythical Creature/Animal/Object \n(whatever you'd like really):", font=("Comic Sans MS", 15), bg='lightgreen').place(x=30, y=230)
	

    name_entry = Entry(ml6_wn, width=19)
    name_entry.place(x=420, y=73)

    club_entry = Entry(ml6_wn, width=19)
    club_entry.place(x=420, y=115)

    new_name_entry = Entry(ml6_wn, width=19)
    new_name_entry.place(x=420, y=155)

    pn_entry = Entry(ml6_wn, width=19)
    pn_entry.place(x=420, y=195)

    mc_entry = Entry(ml6_wn, width=19)
    mc_entry.place(x=420, y=245)
    
    
    submit_btn = Button(ml6_wn, text="Submit", background="red", font=('Comic Sans MS', 12), command=lambda: finish_madlib(ml6_wn, name_entry.get(), club_entry.get(), new_name_entry.get(), pn_entry.get(), mc_entry.get()))
    submit_btn.place(x=272, y=320)

    ml6_wn.mainloop()
    
    
    
root = Tk()
root.title("Jaia's Madlibs")
root.geometry('515x500')
root.config (bg="maroon")
root.resizable(False, False)

# Adding an icon to the main window
photo = ImageTk.PhotoImage(Image.open('icon.png'))
root.iconphoto(False, photo)

Label(root, font=("Comic Sans MS", 16), text= "Welcome To Jaia's Madlibs", bg='maroon').place(x=120, y=0)

ml1 = Button(root, text='Injured Fish', font=("Comic Sans MS", 16), command=lambda: first_madlib(root, photo), bg='white')
ml1.place(x=193, y=150)

ml2 = Button(root, text='Archer!!!', font=("Comic Sans MS", 16), command=lambda: second_madlib(root, photo), bg='pink')
ml2.place(x=213, y=90)

ml3 = Button(root, text="Chowder's Peculiar Dream", font=("Comic Sans MS", 16), command=lambda: third_madlib(root, photo), bg='white')
ml3.place(x=125, y=390)

ml4 = Button(root, text="Slinkman's Warning", font=("Comic Sans MS", 16), command=lambda: fourth_madlib(root, photo), bg='white')
ml4.place(x=155, y=270)

ml5 = Button(root, text="Mandy's Intrusion", font=("Comic Sans MS", 16), command=lambda: fifth_madlib(root, photo), bg='pink')
ml5.place(x=163, y=210)

ml6 = Button(root, text = "Down With The Sickness", font=("Comic Sans MS", 16), command=lambda: sixth_madlib(root, photo), bg='pink')
ml6.place(x=133, y=330)

root.update()
root.mainloop()