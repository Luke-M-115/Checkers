import time
import os
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

log.grid(row=5,rowspan=2,column=11,columnspan=2,sticky=W+E)

log.configure(state='disabled')


def end():
    root.destroy()


global text
text=''
def clear():
    log.configure(state='normal')
    log.delete(1.0,END)
    log.configure(state='disabled')

def redmove(num):
    global text
    text=text+"\nred"+str(num)
    log.configure(state='normal')
    log.insert(1.0,"\nred"+str(num))
    log.configure(state='disabled')
    print(text)

def blackmove(num):
    global text
    text=text+"\nblack"+str(num)
    log.configure(state='normal')
    log.insert(1.0,"\nblack"+str(num))
    log.configure(state='disabled')
    print(text)




LogLable = Label(root,text='LOG',font=12,bg="grey",width=36,borderwidth=2,relief="solid")
spacerlable = Label(root,text="",bg="green",width=15)
scorelable = Label(root,text = "Scoreboard",font=12,bg="lightgreen",width=32,borderwidth=3,relief="ridge")
redscorelable = Label(root,text="RED\n\n#",font=12,bg="red",anchor=N,width=10)
blackscorelable = Label(root,text="BLACK\n\n#",font=12,fg="white",bg="black",anchor=N,width=10)

LogLable.grid(row=4,column=11,columnspan=2,sticky=SW+E)
spacerlable.grid(row=5,column=9,columnspan=2,sticky=NE)
scorelable.grid(row=1,column=11,columnspan=2,sticky=SW+E)
blackscorelable.grid(row=2,column=11,sticky=NW+E)
redscorelable.grid(row=2,column=12,sticky=NW+E)

scroll.grid(row=5,rowspan=2,column=14,sticky=W+N+S)
scroll.config(command=log.yview)

kill = Button(root,height=4,width=30,command=lambda: end(),text = "Exit Game",font=40,bg='grey')
kill.grid(row = 8,column = 11,columnspan = 2)  

clearlog = Button(root,height=1,width=10,command=lambda: clear(),text="Clear Log",bg='grey')  
clearlog.grid(row=7,column=11,sticky=NW)
red1 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(1))
red2 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(2))
red3 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(3))
red4 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(4))
red5 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(5))
red6 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(6))
red7 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(7))
red8 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(8))
red9 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(9))
red10 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(15))
red11 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(11))
red12 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(12))
red13 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(13))
red14 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(14))
red15 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(15))
red16 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(16))
red17 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(17))
red18 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(18))
red19 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(19))
red20 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(20))
red21 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(21))
red22 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(22))
red23 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(23))
red24 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(24))
red25 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(25))
red26 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(26))
red27 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(27))
red28 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(28))
red29 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(29))
red30 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(30))
red31 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(31))
red32 = Button(root, bg="red" ,height = 7, width = 15, command=lambda: redmove(32))



black1 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(1))
black2 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(2))
black3 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(3))
black4 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(4))
black5 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(5))
black6 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(6))
black7 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(7))
black8 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(8))
black9 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(9))
black10 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(15))
black11 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(11))
black12 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(12))
black13 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(13))
black14 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(14))
black15 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(15))
black16 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(16))
black17 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(17))
black18 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(18))
black19 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(19))
black20 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(20))
black21 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(21))
black22 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(22))
black23 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(23))
black24 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(24))
black25 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(25))
black26 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(26))
black27 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(27))
black28 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(28))
black29 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(29))
black30 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(30))
black31 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(31))
black32 = Button(root, bg="black" ,height = 7, width = 15, command=lambda: blackmove(32))

black1.grid(row=1,column=0)
black2.grid(row=1,column=2)
black3.grid(row=1,column=4)
black4.grid(row=1,column=6)
red1.grid(row=1,column=1)
red2.grid(row=1,column=3)
red3.grid(row=1,column=5)
red4.grid(row=1,column=7)

black5.grid(row=2,column=1)
black6.grid(row=2,column=3)
black7.grid(row=2,column=5)
black8.grid(row=2,column=7)
red5.grid(row=2,column=0)
red6.grid(row=2,column=2)
red7.grid(row=2,column=4)
red8.grid(row=2,column=6)

black9.grid(row=3,column=0)
black10.grid(row=3,column=2)
black11.grid(row=3,column=4)
black12.grid(row=3,column=6)
red9.grid(row=3,column=1)
red10.grid(row=3,column=3)
red11.grid(row=3,column=5)
red12.grid(row=3,column=7)

black13.grid(row=4,column=1)
black14.grid(row=4,column=3)
black15.grid(row=4,column=5)
black16.grid(row=4,column=7)
red13.grid(row=4,column=0)
red14.grid(row=4,column=2)
red15.grid(row=4,column=4)
red16.grid(row=4,column=6)

black17.grid(row=5,column=0)
black18.grid(row=5,column=2)
black19.grid(row=5,column=4)
black20.grid(row=5,column=6)
red17.grid(row=5,column=1)
red18.grid(row=5,column=3)
red19.grid(row=5,column=5)
red20.grid(row=5,column=7)

black21.grid(row=6,column=1)
black22.grid(row=6,column=3)
black23.grid(row=6,column=5)
black24.grid(row=6,column=7)
red21.grid(row=6,column=0)
red22.grid(row=6,column=2)
red23.grid(row=6,column=4)
red24.grid(row=6,column=6)

black25.grid(row=7,column=0)
black26.grid(row=7,column=2)
black27.grid(row=7,column=4)
black28.grid(row=7,column=6)
red25.grid(row=7,column=1)
red26.grid(row=7,column=3)
red27.grid(row=7,column=5)
red28.grid(row=7,column=7)

black29.grid(row=8,column=1)
black30.grid(row=8,column=3)
black31.grid(row=8,column=5)
black32.grid(row=8,column=7)
red29.grid(row=8,column=0)
red30.grid(row=8,column=2)
red31.grid(row=8,column=4)
red32.grid(row=8,column=6)


root.mainloop()

clearscreen()