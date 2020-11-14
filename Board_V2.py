import time
import os
import moves
from tkinter import *

clearscreen = lambda: os.system('cls')
clearscreen()

root = Tk()
root.configure(bg='green')
root.title("Checkers")
root.geometry("1000x750+0+0")
root.attributes("-fullscreen", True)
root.bind("<F11>", lambda event: root.attributes("-fullscreen", not root.attributes("-fullscreen")))

root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

scroll = Scrollbar(root)

log = Text(root,height = 14,width=30,yscrollcommand = scroll.set)

log.grid(row=4,rowspan=2,column=11,columnspan=2,sticky=W+E)

log.configure(state='disabled')    

def end():
    root.destroy()

global text
text=''

def clear():
    log.configure(state='normal')
    log.delete(1.0,END)
    log.configure(state='disabled')

def redmove(row,col):
    global text
    poss_M = moves.possible_moves(row,col,0)
    text=text+"\nred "+str(row)+"-"+str(col)+" "+poss_M
    log.configure(state='normal')
    log.insert(1.0,"\nred "+str(row)+"-"+str(col)+" "+poss_M)
    log.configure(state='disabled')
    

def blackmove(row,col):
    global text
    poss_M = moves.possible_moves(row,col,1)
    text=text+"\nblack"+str(row)+"-"+str(col)+" "+poss_M
    log.configure(state='normal')
    log.insert(1.0,"\nblack "+str(row)+"-"+str(col)+" "+poss_M)
    log.configure(state='disabled')

def map(row,col,color,black,red):
        
    if color == 1:
        red[row][col].configure(command=lambda: redmove(row,col))
    else:
        black[row][col].configure(command=lambda: blackmove(row,col) )   
    

LogLable = Label(root,text='LOG',font=12,bg="grey",width=36,borderwidth=2,relief="solid")
spacerlable = Label(root,text="",bg="green",width=15)
scorelable = Label(root,text = "Scoreboard",font=12,bg="lightgreen",width=32,borderwidth=3,relief="ridge")
redscorelable = Label(root,text="RED\n\n#",font=12,bg="red",anchor=N,width=10)
blackscorelable = Label(root,text="BLACK\n\n#",font=12,fg="white",bg="black",anchor=N,width=10)

LogLable.grid(row=3,column=11,columnspan=2,sticky=SW+E)
spacerlable.grid(row=4,column=9,columnspan=2,sticky=NE)
scorelable.grid(row=0,column=11,columnspan=2,sticky=SW+E)
blackscorelable.grid(row=1,column=11,sticky=NW+E)
redscorelable.grid(row=1,column=12,sticky=NW+E)

scroll.grid(row=4,rowspan=2,column=14,sticky=W+N+S)
scroll.config(command=log.yview)

kill = Button(root,height=4,width=30,command=lambda: end(),text = "Exit Game",font=40,bg='grey')
kill.grid(row = 7,column = 11,columnspan = 2)  

clearlog = Button(root,height=1,width=10,command=lambda: clear(),text="Clear Log",bg='grey')  
clearlog.grid(row=6,column=11,sticky=NW)



red = []
black = []
for i in range(8): 
    col = [] 
    for j in range(8): 
        col.append(0)       
    red.append(col)
    black.append(col)

swap = 0
for i in range(0,8):
    for j in range(0,8): 
        if swap == 1:
            red[i][j] = Button(root, bg="red" ,height = 7, width = 15)
            red[i][j].grid(row=i,column=j)
            swap = 0

        else:
            black[i][j] = Button(root, bg="black" ,height = 7, width = 15)
            black[i][j].grid(row=i,column=j)
            swap = 1
    if swap ==1:
        swap = 0
    else: 
        swap = 1   

swap = 1
for i in range(0,8):
    for j in range(0,8): 
        if swap == 1:
            map(i,j,0,black,red)
            swap = 0

        else:
            map(i,j,1,black,red)
            swap = 1
    if swap ==1:
        swap = 0
    else: 
        swap = 1 


root.mainloop()

clearscreen()