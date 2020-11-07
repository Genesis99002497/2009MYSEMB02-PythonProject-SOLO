## import libraries

from tkinter import *

import playsound as playsound
from gtts import gTTS
from playsound import playsound

################### Initialized window####################

root = Tk()
root.geometry('450x300')
root.resizable(0,0)
root.config(bg = 'white')
root.title('Player - Text_to_Voice')

p1 = PhotoImage(file='lnt.png')

##Heading
Label(root, text = 'Text To Speech' , font='arial 24 bold' , bg ='white').pack()
Label(root, text ='Mini-Project : Yash Raj , Pranav Pandhi' , font ='arial 15 bold', bg = 'white').pack(side = BOTTOM)

#Label
Label(root, text ='Enter Text', font ='arial 15 bold', bg ='white').place(x=20,y=60)

##Text Variable
Msg = StringVar()

#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=20 , y=100)

###################define function##############################
from testfunction import read_successful
from testfunction import sound_successful
def Text_to_Voice():

    Message = entry_field.get()
    speech = gTTS(text = Message)
    print(read_successful(10))
    speech.save('Player.mp3')
    playsound('Player.mp3')
    print(sound_successful(20))

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'arial 15 bold', command = Text_to_Voice, width =4).place(x=25, y=140)
Button(root,text = 'EXIT',font = 'arial 15 bold' , command = Exit, bg = 'red').place(x=100,y=140)
Button(root, text = 'RESET', font='arial 15 bold', command = Reset).place(x=175 , y =140)

#infinite loop to run program
root.mainloop()


