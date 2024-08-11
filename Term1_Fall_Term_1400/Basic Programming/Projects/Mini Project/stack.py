<<<<<<< HEAD

from tkinter import *
from random import *
from PIL import Image, ImageTk





master = Tk()
bomb_positions = []

ico = Image.open('min.png')
photo = ImageTk.PhotoImage(ico)
master.wm_iconphoto(False, photo)
master.title('Minesweeper')




bmb_index = []
for k in range(10**3) :
    bmb_index = list(bmb_index)
    bmb_index.append(randint(0, 144))
    bmb_index = set(bmb_index)
    if len(bmb_index) == 20 :
        break
bmb_index = list(bmb_index)

def function3(event):
    print("Function3")


def place_flag(square):
    print("PlaceFlag")
    btnList[square]['text'] = u'\u2690'

def check(square,btn):
    print("Check ",square, btn)
    if square in bomb_positions:
        print("Booommmmm!!!")
        btnList[square]['text'] = u'\u273A'
    else:
        def emtehan(i) :
            global bmb_index
            shakhes = 0
            lst_hamsaye = [i-1, i+1, i-10, i+10, i-9, i+9, i-8, i+8]
            for ozv in lst_hamsaye :
                if ozv in bmb_index :
                    shakhes+=1

            return shakhes
        print(str(emtehan(square)))
        btnList[square]['text'] = str(emtehan(square))

def setFocus(event):
    event.widget.focus_set()

btnList = []

for i in range (81):

    

    
    row, col = divmod(i,9)

    btn = Button(master, width=4, height = 2)
    
    btn.grid(row=row, column=col)



    if i not in bmb_index :                              #These are 'safe' buttons
        btn = Button(master, width=4 , height = 2)
        btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i,btn))

        btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i)) 
                                  

        btn.grid(row=row, column=col)



    if i in bmb_index :                              #These are 'bombs'
        btn = Button(master, width=4, height = 2)
        btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i,btn))
        btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))  
        btn.grid(row=row, column=col)
        bomb_positions.append(i)
    
    btnList.append(btn)
    btn.bind("<Enter>",setFocus)
    



master.mainloop()


=======

from tkinter import *
from random import *
from PIL import Image, ImageTk





master = Tk()
bomb_positions = []

ico = Image.open('min.png')
photo = ImageTk.PhotoImage(ico)
master.wm_iconphoto(False, photo)
master.title('Minesweeper')




bmb_index = []
for k in range(10**3) :
    bmb_index = list(bmb_index)
    bmb_index.append(randint(0, 144))
    bmb_index = set(bmb_index)
    if len(bmb_index) == 20 :
        break
bmb_index = list(bmb_index)

def function3(event):
    print("Function3")


def place_flag(square):
    print("PlaceFlag")
    btnList[square]['text'] = u'\u2690'

def check(square,btn):
    print("Check ",square, btn)
    if square in bomb_positions:
        print("Booommmmm!!!")
        btnList[square]['text'] = u'\u273A'
    else:
        def emtehan(i) :
            global bmb_index
            shakhes = 0
            lst_hamsaye = [i-1, i+1, i-10, i+10, i-9, i+9, i-8, i+8]
            for ozv in lst_hamsaye :
                if ozv in bmb_index :
                    shakhes+=1

            return shakhes
        print(str(emtehan(square)))
        btnList[square]['text'] = str(emtehan(square))

def setFocus(event):
    event.widget.focus_set()

btnList = []

for i in range (81):

    

    
    row, col = divmod(i,9)

    btn = Button(master, width=4, height = 2)
    
    btn.grid(row=row, column=col)



    if i not in bmb_index :                              #These are 'safe' buttons
        btn = Button(master, width=4 , height = 2)
        btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i,btn))

        btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i)) 
                                  

        btn.grid(row=row, column=col)



    if i in bmb_index :                              #These are 'bombs'
        btn = Button(master, width=4, height = 2)
        btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i,btn))
        btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))  
        btn.grid(row=row, column=col)
        bomb_positions.append(i)
    
    btnList.append(btn)
    btn.bind("<Enter>",setFocus)
    



master.mainloop()


>>>>>>> deba06a (BP Projects Added)
