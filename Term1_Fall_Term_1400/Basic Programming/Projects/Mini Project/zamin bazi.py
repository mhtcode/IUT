<<<<<<< HEAD
import smtplib
import sys
import time as ts
from email.message import EmailMessage
from random import randint
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

reps = 0


def history():
    history = (tedad_vorood, tedad_bord, tedad_bakht)

    print(f'tedadvorood : {tedad_vorood}')
    print(f'tedadbord : {tedad_bord}')
    print(f'tedadbakht : {tedad_bakht}')


def send_email_admin(msg, tedad_vorood, tedad_bord, tedad_bakht):

    global email_guest
    global a
    with open('database.txt', 'r') as f1:
        lst_lines_f = f1.readlines()

    email = EmailMessage()

    email['from'] = 'masihtanoursaz01@gmail.com'

    efrom = email['from']

    password = 'M@sih127'

    email['to'] = email_guest
    if a == 1:
        email['subject'] = f"Welcome back {msg} , I know you've enjoyed my game. "
    else:
        email['subject'] = f"Welcome {msg} , I know you'll enjoy my game. "

    lst_vorood = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh',
                  'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth',
                  'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth', 'Nineteenth', 'Twentieth',
                  'Twenty-first', 'Twenty-second', 'Twenty-third', 'Twenty-fourth', 'Twenty-fifth',
                  'Twenty-Sixth', 'Twenty-seventh', 'Twenty-eighth', 'Twenty-ninth', 'Thirtieth']

    try:
        email.set_content(f''' This is your {lst_vorood[tedad_vorood-1]} entry
                            It's yor game history :
                                        tedad_bord = {tedad_bord}
                                        tedad_bakht = {tedad_bakht}

                                        Give me your feedback about game please (◠‿◠) ''')
    except:
        print("▶►▸ You entered more than '30' if you want play again you should buy license from MTC(Masih Tanoursaz company) ◂◄◀")
        for i in range(5):
            ts.sleep(1)
            print('\a')
        print("That was just a joke.To play again, just login with another name (◠‿◠)")
        quit()

    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

            smtp.ehlo()

            smtp.starttls()

            smtp.login(efrom, password)

            smtp.send_message(email)

            print('Email was sent!\a')
    except:

        print("Email wasn't sent! try again later!\a")


def emtehan(i):
    global n
    global m
    global masahat_zamin

    shakhes = 0

    satr, sotoon = divmod(i, n)

    if satr != 0 and sotoon != 0:
        lst_hamsaye = [i-1, i+1, i-n-1, i+n+1, i-n, i+n, i-n+1, i+n-1]

    elif satr == 0 and i != 0 and i != n-1:
        lst_hamsaye = [i-1, i+n-1, i+n, i+n+1, i+1]

    elif satr == m-1 and i != masahat_zamin-1-n and i != masahat_zamin - 1:
        lst_hamsaye = [i-1, i+1, i-n-1, i-n, i-n+1]

    elif sotoon == 0 and i != 0 and i != masahat_zamin-1-n:
        lst_hamsaye = [i-n, i-n+1, i+n, i+n+1, i+1]
    elif sotoon == n-1 and i != n-1 and i != masahat_zamin - 1:
        lst_hamsaye = [i-n, i+n, i-n-1, i-1, i+n-1]

    else:
        if i == 0:
            lst_hamsaye = [i+1, i+n+1,  i+n]
        elif i == n-1:
            lst_hamsaye = [i-1, i+n-1,  i+n]
        elif i == (masahat_zamin-1-n):
            lst_hamsaye = [i+1, i-n+1,  i-n]
        elif i == (masahat_zamin - 1):
            lst_hamsaye = [i-1, i-n-1,  i-n]

    for ozv in lst_hamsaye:
        if ozv in bmb_index:
            shakhes += 1

    return shakhes


def Minesweeper():
    global tedad_vorood
    print('You can play again now \a')
    zamin_bazi = input('''Choose the siza of board ==> 
                                1:(9*9)
                                2:(12*12)
                                3:(15*20)
                                Enter the according to size of the board (1 or 2 or 3) : ''')

    try:
        while int(zamin_bazi) not in [1, 2, 3]:

            print('<< Enter the right number please >>')

            zamin_bazi = input('''Choose the siza of board ==> 1:(9*9)
                                    2:(12*12)
                                    3:(15*20)
                                    Enter the according to size of the board (1 or 2 or 3) : ''')
    except:
        print()
        print('******************************* Error *******************************')
        print('<< Run again and enter the integer according to size of the board\a >>')
        sys.exit()

    if zamin_bazi == '1':
        n = 9
        m = 9
        masahat_zamin = n*m
        tedad_bomb = 10
        tedad_flag = 10
    elif zamin_bazi == '2':
        n = 12
        m = 12
        masahat_zamin = n*m
        tedad_bomb = 20
        tedad_flag = 20
    elif zamin_bazi == '3':
        n = 15
        m = 20
        masahat_zamin = n*m
        tedad_bomb = 40
        tedad_flag = 40

    if masahat_zamin == 300:
        masahat_timer = (1000, 520, 5)
    elif masahat_zamin == 144:
        masahat_timer = (900, 348, 50)
    else:
        masahat_timer = (800, 288, 100)

    master = Tk()
    master.geometry(
        f'{masahat_zamin+masahat_timer[0]}x{masahat_zamin+masahat_timer[1]}')
    master.title('Minesweeper')
    bomb_positions = []

    ico = Image.open(r'min.png')
    photo = ImageTk.PhotoImage(ico)
    master.wm_iconphoto(False, photo)

    bmb_index = []
    for k in range(10**3):
        bmb_index = list(bmb_index)
        bmb_index.append(randint(0, n*m))
        bmb_index = set(bmb_index)
        if len(bmb_index) == tedad_bomb:

            break
    bmb_index = list(bmb_index)

    flag_index = []

    def place_flag(square):
        global tedad_flag
        global tedad_bord
        print("PlaceFlag")
        tedad_flag -= 1
        print(f'You have {tedad_flag} flags \a')
        btnList[square]['text'] = u'\u2690'
        flag_index.append(square)
        if tedad_flag == 0:
            print('It was your last flag\a')
        if tedad_flag < 0:
            print('Error you used all your flags \a')
            master.destroy()

        s = 0

        for i in flag_index:
            if i in bomb_positions:
                s += 1
            if s == len(bomb_positions):
                print('Congratulation')
                print('You win\a')
                tedad_bord_index = lst_lines_f.index(esm) + 1
                tedad_bord = int(lst_lines_f[tedad_bord_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bord_index] = tedad_bord

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)
                ts.sleep(1)
                master.destroy()
                k = input(
                    '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
                if k == '2':
                    o = input(
                        'Are you sure? Do you want to exit?(yes or no) : \a')
                    o.lower()
                if k == "1":

                    Minesweeper()

                elif k == "2" and o == 'yes':
                    ts.sleep(1)

                    z = 0
                    for satr in range(m):
                        for sotoon in range(n):
                            if sotoon == n-1:
                                if z in bmb_index:
                                    print('✺')
                                else:
                                    print('☑')
                                z += 1
                            else:
                                if z in bmb_index:
                                    print('✺', end=' ')
                                else:
                                    print('☑', end=' ')
                                z += 1

                    print(list(map(lambda i: i+1, bomb_positions)))
                    quit()

    def check(square, btn):
        print("Check ", square, btn)
        if square in bomb_positions:
            print("Booommmmm!!!\a")

            btnList[square]['text'] = u'\u273A'
            messagebox.showinfo("Lose", " You lose")
            # with open('database.txt', 'r') as f1:
            #     lst_lines_f = f1.readlines()

            # update tedad bakht
            if tedad_vorood != 1:
                tedad_bakht_index = lst_lines_f.index(esm) + 2
                tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bakht_index] = tedad_bakht

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)

            ts.sleep(1)
            master.destroy()
            k = input('''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 if you want see your game history enter else : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()

            if k == "1":

                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))

                quit()

        else:

            print(str(emtehan(square)))
            btnList[square]['text'] = str(emtehan(square))

    def setFocus(event):
        event.widget.focus_set()

    btnList = []

    for i in range(n*m):

        row, col = divmod(i, n)

        # btn = Button(master, width=4, height = 2)

        # btn.grid(row=row, column=col)

        if i not in bmb_index:  # These are 'safe' buttons
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))

            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))

            btn.grid(row=row, column=col)

        if i in bmb_index:  # These are 'bombs'
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))
            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))
            btn.grid(row=row, column=col)
            bomb_positions.append(i)

        btnList.append(btn)
        btn.bind("<Enter>", setFocus)

    '''--------------------------------- Timer box --------------------------------'''
    time = 5 * masahat_zamin

    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    work_sec = time
    timer = None

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        master.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f'{time}')
        title_label.config(text="Timer")

        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):

        count_sec = count

        canvas.itemconfig(timer_text, text=f"{count_sec}")
        if count > 0:
            global timer
            timer = master.after(1000, count_down, count - 1)
        else:
            messagebox.showinfo("Time countdown", "Time's Up = > You lose")
            print("Time's Up = > You lose\a")

            # update tedad bakht
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":

                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))
                quit()

    timer_in_zamin_1 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_2 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_3 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=start_timer)
    reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=reset_timer)
    exit_button = Button(bg="#F1583F", fg="#fff", text="Exit", command=quit)

    if zamin_bazi == '1':
        ax_timer = (450, 20)

        start_button.place(
            x=timer_in_zamin_1['start'][0], y=timer_in_zamin_1['start'][1])

        reset_button.place(
            x=timer_in_zamin_1['reset'][0], y=timer_in_zamin_1['reset'][1])

        exit_button.place(
            x=timer_in_zamin_1['exit'][0], y=timer_in_zamin_1['exit'][1])

    if zamin_bazi == '2':
        ax_timer = (600, 65)

        start_button.place(
            x=timer_in_zamin_2['start'][0], y=timer_in_zamin_2['start'][1])

        reset_button.place(
            x=timer_in_zamin_2['reset'][0], y=timer_in_zamin_2['reset'][1])

        exit_button.place(
            x=timer_in_zamin_2['exit'][0], y=timer_in_zamin_2['exit'][1])

    if zamin_bazi == '3':
        ax_timer = (750, 150)

        start_button.place(
            x=timer_in_zamin_3['start'][0], y=timer_in_zamin_3['start'][1])

        reset_button.place(
            x=timer_in_zamin_3['reset'][0], y=timer_in_zamin_3['reset'][1])

        exit_button.place(
            x=timer_in_zamin_3['exit'][0], y=timer_in_zamin_3['exit'][1])

    # label
    title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    title_label.place(x=masahat_timer[0] -
                      masahat_timer[2], y=masahat_timer[1]//2)

    # config UI for canvas
    canvas = Canvas(width=200, height=224,  highlightthickness=0)
    timer_img = PhotoImage(file="timer01.png")
    canvas.create_image(100, 112, image=timer_img)
    timer_text = canvas.create_text(
        100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
    canvas.place(x=ax_timer[0], y=ax_timer[1])

    master.mainloop()


matn = '''Hi, 
In Minesweeper, mines (that resemble naval mines in the classic theme) are scattered throughout a board, which is divided into cells.
Cells have three states: uncovered, covered and flagged. 
A covered cell is blank and clickable, while an uncovered cell is exposed. 
Flagged cells are those marked by the player to indicate a potential mine location.

A player left-clicks a cell to uncover it. If a player uncovers a mined cell, the game ends, as there is only 1 life per game.
Otherwise, the uncovered cell displays either a number, indicating the number of mines diagonally and/or adjacent to it, or a blank tile (or "0").

Right-clicking on a cell will flag it, causing a flag to appear on it. 
Flagged cells are still considered covered, and a player can click on them to uncover them, although typically they must first be unflagged with an additional right-click.

To win the game, players must uncover all non-mine cells, at which point, the timer is stopped. Flagging all the mined cells is not required.'''

border = '''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

print(border, '\n')
print(matn, '\n')
print(border)


with open('database.txt', 'a+') as f:

    name = input('Enter your name please : ')

    zamin_bazi = input('''Choose the siza of board ==> 
                                1:(9*9)
                                2:(12*12)
                                3:(15*20)
                                Enter an integer according to size of the board (1 or 2 or 3) : ''')

    try:
        while int(zamin_bazi) not in [1, 2, 3]:

            print('<< Enter the right number please >>')

            zamin_bazi = input('''Choose the siza of board ==>
                                    1:(9*9)
                                    2:(12*12)
                                    3:(15*20)
                                    Enter an integar according to size of the board (1 or 2 or 3) : ''')
    except:
        print()
        print('******************************* Error *******************************')
        print('<< Run again and enter the integer according to size of the board\a >>')
        print('*********************************************************************')
        sys.exit()

    if zamin_bazi == '1':
        n = 9
        m = 9
        masahat_zamin = n*m
        tedad_bomb = 10
        tedad_flag = 10
    elif zamin_bazi == '2':
        n = 12
        m = 12
        masahat_zamin = n*m
        tedad_bomb = 20
        tedad_flag = 20
    elif zamin_bazi == '3':
        n = 15
        m = 20
        masahat_zamin = n*m
        tedad_bomb = 40
        tedad_flag = 40

    esm = name+'\n'
    with open('database.txt', 'r') as f1:
        lst_lines_f = f1.readlines()

    if esm in lst_lines_f:
        password2 = input('Enter your game password please : ')

        namepass2 = set({})
        namepass2.add((name, password2))
        namepass2 = str(namepass2)+'\n'
        name_pass3 = f"namepass : {namepass2}"
        if name_pass3 in lst_lines_f:

            a = 1
            mail_index = lst_lines_f.index(esm) + 5

            # update tedad vorood
            tedad_vorood_index = lst_lines_f.index(esm) + 3
            tedad_vorood = int(lst_lines_f[tedad_vorood_index]) + 1
            tedad_bord_index = lst_lines_f.index(esm) + 1
            tedad_bord = int(lst_lines_f[tedad_bord_index])
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index])
            if tedad_vorood == 0:
                tedad_vorood = 0
                tedad_bord = 0
                tedad_bakht = 0

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_vorood_index] = tedad_vorood
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            email_guest = lst_lines_f[mail_index][:-1]

            print(f'Welcome back {name}\n')

            print(f'tedadvorood : {tedad_vorood}\n')
            print(f'tedadbakht : {tedad_bakht}\n')

            send_email_admin(name, tedad_vorood, tedad_bord, tedad_bakht)
        else:
            print(
                'You have entered wrong password or your name exist in databese (choose another name)\a')
            sys.exit()

    else:
        email_guest = input('Enter your email please : ')
        a = 0
        namepass1 = set({})
        password1 = input('Enter your game password please : ')
        namepass1.add((name, password1))
        tedad_vorood = 1
        tedad_bord = 0
        tedad_bakht = 0
        f.write(f'{name}\n')
        f.write(f'{tedad_bord}\n')
        f.write(f'{tedad_bakht}\n')
        f.write(f'{tedad_vorood}\n')
        f.write(f'namepass : {namepass1}\n')
        f.write(email_guest)
        f.write('\n---------------------------------------------\n')
        print(f'Welcome {name}\n')
        print(f'tedadvorood : {tedad_vorood}\n')
        send_email_admin(name, tedad_vorood, tedad_bord, tedad_bakht)

    if masahat_zamin == 300:
        masahat_timer = (1000, 520, 5)
    elif masahat_zamin == 144:
        masahat_timer = (900, 348, 50)
    else:
        masahat_timer = (800, 288, 100)

    master = Tk()
    master.geometry(
        f'{masahat_zamin+masahat_timer[0]}x{masahat_zamin+masahat_timer[1]}')
    master.title('Minesweeper')
    bomb_positions = []

    ico = Image.open('min.png')
    photo = ImageTk.PhotoImage(ico)
    master.wm_iconphoto(False, photo)

    bmb_index = []
    for k in range(10**3):
        bmb_index = list(bmb_index)
        bmb_index.append(randint(0, n*m))
        bmb_index = set(bmb_index)
        if len(bmb_index) == tedad_bomb:
            break
    bmb_index = list(bmb_index)

    flag_index = []

    def place_flag(square):
        global tedad_flag
        global tedad_bord
        print("PlaceFlag")
        tedad_flag -= 1
        print(f'You have {tedad_flag} flags \a')
        btnList[square]['text'] = u'\u2690'
        flag_index.append(square)
        if tedad_flag == 0:
            print('It was your last flag\a')
        if tedad_flag < 0:
            print('Error you used all your flags \a')
            master.destroy()

        s = 0

        for i in flag_index:
            if i in bomb_positions:
                s += 1
            if s == len(bomb_positions):
                print('Congratulation')
                print('You win\a')
                tedad_bord_index = lst_lines_f.index(esm) + 1
                tedad_bord = int(lst_lines_f[tedad_bord_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bord_index] = tedad_bord

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)
                ts.sleep(1)
                master.destroy()
                k = input(
                    '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
                if k == '2':
                    o = input(
                        'Are you sure? Do you want to exit?(yes or no) : \a')
                    o.lower()
                if k == "1":

                    Minesweeper()

                elif k == "2" and o == 'yes':
                    ts.sleep(1)

                    z = 0
                    for satr in range(m):
                        for sotoon in range(n):
                            if sotoon == n-1:
                                if z in bmb_index:
                                    print('✺')
                                else:
                                    print('☑')
                                z += 1
                            else:
                                if z in bmb_index:
                                    print('✺', end=' ')
                                else:
                                    print('☑', end=' ')
                                z += 1

                    print(list(map(lambda i: i+1, bomb_positions)))

                    quit()

    def check(square, btn):
        print("Check ", square, btn)
        if square in bomb_positions:
            print("Booommmmm!!!\a")

            btnList[square]['text'] = u'\u273A'
            messagebox.showinfo("Lose", " You lose")
            with open('database.txt', 'r') as f1:
                lst_lines_f = f1.readlines()

            # update tedad bakht
            # if tedad_vorood != 1:
                tedad_bakht_index = lst_lines_f.index(esm) + 2
                tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bakht_index] = tedad_bakht

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)

            ts.sleep(1)
            master.destroy()
            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":

                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))

                quit()

        else:

            print(str(emtehan(square)))
            btnList[square]['text'] = str(emtehan(square))

    def setFocus(event):
        event.widget.focus_set()

    btnList = []

    for i in range(n*m):

        row, col = divmod(i, n)

        # btn = Button(master, width=4, height = 2)

        # btn.grid(row=row, column=col)

        if i not in bmb_index:  # These are 'safe' buttons
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))

            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))

            btn.grid(row=row, column=col)

        if i in bmb_index:  # These are 'bombs'
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))
            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))
            btn.grid(row=row, column=col)
            bomb_positions.append(i)

        btnList.append(btn)
        btn.bind("<Enter>", setFocus)

    '''--------------------------------- Timer box --------------------------------'''
    time = 5 * masahat_zamin

    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    work_sec = time
    timer = None

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        master.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f'{time}')
        title_label.config(text="Timer")

        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):

        count_sec = count

        canvas.itemconfig(timer_text, text=f"{count_sec}")
        if count > 0:
            global timer
            timer = master.after(1000, count_down, count - 1)
        else:
            messagebox.showinfo("Time countdown", "Time's Up = > You lose")
            print("Time's Up = > You lose\a")

            # update tedad bakht
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":
                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()
            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))
                quit()

    timer_in_zamin_1 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_2 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_3 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=start_timer)
    reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=reset_timer)
    exit_button = Button(bg="#F1583F", fg="#fff", text="Exit", command=quit)

    if zamin_bazi == '1':
        ax_timer = (450, 20)

        start_button.place(
            x=timer_in_zamin_1['start'][0], y=timer_in_zamin_1['start'][1])

        reset_button.place(
            x=timer_in_zamin_1['reset'][0], y=timer_in_zamin_1['reset'][1])

        exit_button.place(
            x=timer_in_zamin_1['exit'][0], y=timer_in_zamin_1['exit'][1])

    if zamin_bazi == '2':
        ax_timer = (600, 65)

        start_button.place(
            x=timer_in_zamin_2['start'][0], y=timer_in_zamin_2['start'][1])

        reset_button.place(
            x=timer_in_zamin_2['reset'][0], y=timer_in_zamin_2['reset'][1])

        exit_button.place(
            x=timer_in_zamin_2['exit'][0], y=timer_in_zamin_2['exit'][1])

    if zamin_bazi == '3':
        ax_timer = (750, 150)

        start_button.place(
            x=timer_in_zamin_3['start'][0], y=timer_in_zamin_3['start'][1])

        reset_button.place(
            x=timer_in_zamin_3['reset'][0], y=timer_in_zamin_3['reset'][1])

        exit_button.place(
            x=timer_in_zamin_3['exit'][0], y=timer_in_zamin_3['exit'][1])

    # pause_button = Button(text="Pause", fg="#fff", bg="#F1583F")
    # pause_button.place(
    #     x=masahat_timer[0] - masahat_timer[2], y=masahat_timer[1]//2 + 200)
    # I couldn't find a command (algorithm) for pause btn so if you have an idea about it you can email me #

    # label
    title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    title_label.place(x=masahat_timer[0] -
                      masahat_timer[2], y=masahat_timer[1]//2)

    # config UI for canvas
    canvas = Canvas(width=200, height=224,  highlightthickness=0)
    timer_img = PhotoImage(file="timer01.png")
    canvas.create_image(100, 112, image=timer_img)
    timer_text = canvas.create_text(
        100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
    canvas.place(x=ax_timer[0], y=ax_timer[1])

    master.mainloop()
=======
import smtplib
import sys
import time as ts
from email.message import EmailMessage
from random import randint
from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

reps = 0


def history():
    history = (tedad_vorood, tedad_bord, tedad_bakht)

    print(f'tedadvorood : {tedad_vorood}')
    print(f'tedadbord : {tedad_bord}')
    print(f'tedadbakht : {tedad_bakht}')


def send_email_admin(msg, tedad_vorood, tedad_bord, tedad_bakht):

    global email_guest
    global a
    with open('database.txt', 'r') as f1:
        lst_lines_f = f1.readlines()

    email = EmailMessage()

    email['from'] = 'masihtanoursaz01@gmail.com'

    efrom = email['from']

    password = 'M@sih127'

    email['to'] = email_guest
    if a == 1:
        email['subject'] = f"Welcome back {msg} , I know you've enjoyed my game. "
    else:
        email['subject'] = f"Welcome {msg} , I know you'll enjoy my game. "

    lst_vorood = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh',
                  'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth',
                  'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth', 'Nineteenth', 'Twentieth',
                  'Twenty-first', 'Twenty-second', 'Twenty-third', 'Twenty-fourth', 'Twenty-fifth',
                  'Twenty-Sixth', 'Twenty-seventh', 'Twenty-eighth', 'Twenty-ninth', 'Thirtieth']

    try:
        email.set_content(f''' This is your {lst_vorood[tedad_vorood-1]} entry
                            It's yor game history :
                                        tedad_bord = {tedad_bord}
                                        tedad_bakht = {tedad_bakht}

                                        Give me your feedback about game please (◠‿◠) ''')
    except:
        print("▶►▸ You entered more than '30' if you want play again you should buy license from MTC(Masih Tanoursaz company) ◂◄◀")
        for i in range(5):
            ts.sleep(1)
            print('\a')
        print("That was just a joke.To play again, just login with another name (◠‿◠)")
        quit()

    try:
        with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

            smtp.ehlo()

            smtp.starttls()

            smtp.login(efrom, password)

            smtp.send_message(email)

            print('Email was sent!\a')
    except:

        print("Email wasn't sent! try again later!\a")


def emtehan(i):
    global n
    global m
    global masahat_zamin

    shakhes = 0

    satr, sotoon = divmod(i, n)

    if satr != 0 and sotoon != 0:
        lst_hamsaye = [i-1, i+1, i-n-1, i+n+1, i-n, i+n, i-n+1, i+n-1]

    elif satr == 0 and i != 0 and i != n-1:
        lst_hamsaye = [i-1, i+n-1, i+n, i+n+1, i+1]

    elif satr == m-1 and i != masahat_zamin-1-n and i != masahat_zamin - 1:
        lst_hamsaye = [i-1, i+1, i-n-1, i-n, i-n+1]

    elif sotoon == 0 and i != 0 and i != masahat_zamin-1-n:
        lst_hamsaye = [i-n, i-n+1, i+n, i+n+1, i+1]
    elif sotoon == n-1 and i != n-1 and i != masahat_zamin - 1:
        lst_hamsaye = [i-n, i+n, i-n-1, i-1, i+n-1]

    else:
        if i == 0:
            lst_hamsaye = [i+1, i+n+1,  i+n]
        elif i == n-1:
            lst_hamsaye = [i-1, i+n-1,  i+n]
        elif i == (masahat_zamin-1-n):
            lst_hamsaye = [i+1, i-n+1,  i-n]
        elif i == (masahat_zamin - 1):
            lst_hamsaye = [i-1, i-n-1,  i-n]

    for ozv in lst_hamsaye:
        if ozv in bmb_index:
            shakhes += 1

    return shakhes


def Minesweeper():
    global tedad_vorood
    print('You can play again now \a')
    zamin_bazi = input('''Choose the siza of board ==> 
                                1:(9*9)
                                2:(12*12)
                                3:(15*20)
                                Enter the according to size of the board (1 or 2 or 3) : ''')

    try:
        while int(zamin_bazi) not in [1, 2, 3]:

            print('<< Enter the right number please >>')

            zamin_bazi = input('''Choose the siza of board ==> 1:(9*9)
                                    2:(12*12)
                                    3:(15*20)
                                    Enter the according to size of the board (1 or 2 or 3) : ''')
    except:
        print()
        print('******************************* Error *******************************')
        print('<< Run again and enter the integer according to size of the board\a >>')
        sys.exit()

    if zamin_bazi == '1':
        n = 9
        m = 9
        masahat_zamin = n*m
        tedad_bomb = 10
        tedad_flag = 10
    elif zamin_bazi == '2':
        n = 12
        m = 12
        masahat_zamin = n*m
        tedad_bomb = 20
        tedad_flag = 20
    elif zamin_bazi == '3':
        n = 15
        m = 20
        masahat_zamin = n*m
        tedad_bomb = 40
        tedad_flag = 40

    if masahat_zamin == 300:
        masahat_timer = (1000, 520, 5)
    elif masahat_zamin == 144:
        masahat_timer = (900, 348, 50)
    else:
        masahat_timer = (800, 288, 100)

    master = Tk()
    master.geometry(
        f'{masahat_zamin+masahat_timer[0]}x{masahat_zamin+masahat_timer[1]}')
    master.title('Minesweeper')
    bomb_positions = []

    ico = Image.open(r'min.png')
    photo = ImageTk.PhotoImage(ico)
    master.wm_iconphoto(False, photo)

    bmb_index = []
    for k in range(10**3):
        bmb_index = list(bmb_index)
        bmb_index.append(randint(0, n*m))
        bmb_index = set(bmb_index)
        if len(bmb_index) == tedad_bomb:

            break
    bmb_index = list(bmb_index)

    flag_index = []

    def place_flag(square):
        global tedad_flag
        global tedad_bord
        print("PlaceFlag")
        tedad_flag -= 1
        print(f'You have {tedad_flag} flags \a')
        btnList[square]['text'] = u'\u2690'
        flag_index.append(square)
        if tedad_flag == 0:
            print('It was your last flag\a')
        if tedad_flag < 0:
            print('Error you used all your flags \a')
            master.destroy()

        s = 0

        for i in flag_index:
            if i in bomb_positions:
                s += 1
            if s == len(bomb_positions):
                print('Congratulation')
                print('You win\a')
                tedad_bord_index = lst_lines_f.index(esm) + 1
                tedad_bord = int(lst_lines_f[tedad_bord_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bord_index] = tedad_bord

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)
                ts.sleep(1)
                master.destroy()
                k = input(
                    '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
                if k == '2':
                    o = input(
                        'Are you sure? Do you want to exit?(yes or no) : \a')
                    o.lower()
                if k == "1":

                    Minesweeper()

                elif k == "2" and o == 'yes':
                    ts.sleep(1)

                    z = 0
                    for satr in range(m):
                        for sotoon in range(n):
                            if sotoon == n-1:
                                if z in bmb_index:
                                    print('✺')
                                else:
                                    print('☑')
                                z += 1
                            else:
                                if z in bmb_index:
                                    print('✺', end=' ')
                                else:
                                    print('☑', end=' ')
                                z += 1

                    print(list(map(lambda i: i+1, bomb_positions)))
                    quit()

    def check(square, btn):
        print("Check ", square, btn)
        if square in bomb_positions:
            print("Booommmmm!!!\a")

            btnList[square]['text'] = u'\u273A'
            messagebox.showinfo("Lose", " You lose")
            # with open('database.txt', 'r') as f1:
            #     lst_lines_f = f1.readlines()

            # update tedad bakht
            if tedad_vorood != 1:
                tedad_bakht_index = lst_lines_f.index(esm) + 2
                tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bakht_index] = tedad_bakht

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)

            ts.sleep(1)
            master.destroy()
            k = input('''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 if you want see your game history enter else : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()

            if k == "1":

                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))

                quit()

        else:

            print(str(emtehan(square)))
            btnList[square]['text'] = str(emtehan(square))

    def setFocus(event):
        event.widget.focus_set()

    btnList = []

    for i in range(n*m):

        row, col = divmod(i, n)

        # btn = Button(master, width=4, height = 2)

        # btn.grid(row=row, column=col)

        if i not in bmb_index:  # These are 'safe' buttons
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))

            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))

            btn.grid(row=row, column=col)

        if i in bmb_index:  # These are 'bombs'
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))
            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))
            btn.grid(row=row, column=col)
            bomb_positions.append(i)

        btnList.append(btn)
        btn.bind("<Enter>", setFocus)

    '''--------------------------------- Timer box --------------------------------'''
    time = 5 * masahat_zamin

    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    work_sec = time
    timer = None

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        master.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f'{time}')
        title_label.config(text="Timer")

        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):

        count_sec = count

        canvas.itemconfig(timer_text, text=f"{count_sec}")
        if count > 0:
            global timer
            timer = master.after(1000, count_down, count - 1)
        else:
            messagebox.showinfo("Time countdown", "Time's Up = > You lose")
            print("Time's Up = > You lose\a")

            # update tedad bakht
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":

                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))
                quit()

    timer_in_zamin_1 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_2 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_3 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=start_timer)
    reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=reset_timer)
    exit_button = Button(bg="#F1583F", fg="#fff", text="Exit", command=quit)

    if zamin_bazi == '1':
        ax_timer = (450, 20)

        start_button.place(
            x=timer_in_zamin_1['start'][0], y=timer_in_zamin_1['start'][1])

        reset_button.place(
            x=timer_in_zamin_1['reset'][0], y=timer_in_zamin_1['reset'][1])

        exit_button.place(
            x=timer_in_zamin_1['exit'][0], y=timer_in_zamin_1['exit'][1])

    if zamin_bazi == '2':
        ax_timer = (600, 65)

        start_button.place(
            x=timer_in_zamin_2['start'][0], y=timer_in_zamin_2['start'][1])

        reset_button.place(
            x=timer_in_zamin_2['reset'][0], y=timer_in_zamin_2['reset'][1])

        exit_button.place(
            x=timer_in_zamin_2['exit'][0], y=timer_in_zamin_2['exit'][1])

    if zamin_bazi == '3':
        ax_timer = (750, 150)

        start_button.place(
            x=timer_in_zamin_3['start'][0], y=timer_in_zamin_3['start'][1])

        reset_button.place(
            x=timer_in_zamin_3['reset'][0], y=timer_in_zamin_3['reset'][1])

        exit_button.place(
            x=timer_in_zamin_3['exit'][0], y=timer_in_zamin_3['exit'][1])

    # label
    title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    title_label.place(x=masahat_timer[0] -
                      masahat_timer[2], y=masahat_timer[1]//2)

    # config UI for canvas
    canvas = Canvas(width=200, height=224,  highlightthickness=0)
    timer_img = PhotoImage(file="timer01.png")
    canvas.create_image(100, 112, image=timer_img)
    timer_text = canvas.create_text(
        100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
    canvas.place(x=ax_timer[0], y=ax_timer[1])

    master.mainloop()


matn = '''Hi, 
In Minesweeper, mines (that resemble naval mines in the classic theme) are scattered throughout a board, which is divided into cells.
Cells have three states: uncovered, covered and flagged. 
A covered cell is blank and clickable, while an uncovered cell is exposed. 
Flagged cells are those marked by the player to indicate a potential mine location.

A player left-clicks a cell to uncover it. If a player uncovers a mined cell, the game ends, as there is only 1 life per game.
Otherwise, the uncovered cell displays either a number, indicating the number of mines diagonally and/or adjacent to it, or a blank tile (or "0").

Right-clicking on a cell will flag it, causing a flag to appear on it. 
Flagged cells are still considered covered, and a player can click on them to uncover them, although typically they must first be unflagged with an additional right-click.

To win the game, players must uncover all non-mine cells, at which point, the timer is stopped. Flagging all the mined cells is not required.'''

border = '''--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

print(border, '\n')
print(matn, '\n')
print(border)


with open('database.txt', 'a+') as f:

    name = input('Enter your name please : ')

    zamin_bazi = input('''Choose the siza of board ==> 
                                1:(9*9)
                                2:(12*12)
                                3:(15*20)
                                Enter an integer according to size of the board (1 or 2 or 3) : ''')

    try:
        while int(zamin_bazi) not in [1, 2, 3]:

            print('<< Enter the right number please >>')

            zamin_bazi = input('''Choose the siza of board ==>
                                    1:(9*9)
                                    2:(12*12)
                                    3:(15*20)
                                    Enter an integar according to size of the board (1 or 2 or 3) : ''')
    except:
        print()
        print('******************************* Error *******************************')
        print('<< Run again and enter the integer according to size of the board\a >>')
        print('*********************************************************************')
        sys.exit()

    if zamin_bazi == '1':
        n = 9
        m = 9
        masahat_zamin = n*m
        tedad_bomb = 10
        tedad_flag = 10
    elif zamin_bazi == '2':
        n = 12
        m = 12
        masahat_zamin = n*m
        tedad_bomb = 20
        tedad_flag = 20
    elif zamin_bazi == '3':
        n = 15
        m = 20
        masahat_zamin = n*m
        tedad_bomb = 40
        tedad_flag = 40

    esm = name+'\n'
    with open('database.txt', 'r') as f1:
        lst_lines_f = f1.readlines()

    if esm in lst_lines_f:
        password2 = input('Enter your game password please : ')

        namepass2 = set({})
        namepass2.add((name, password2))
        namepass2 = str(namepass2)+'\n'
        name_pass3 = f"namepass : {namepass2}"
        if name_pass3 in lst_lines_f:

            a = 1
            mail_index = lst_lines_f.index(esm) + 5

            # update tedad vorood
            tedad_vorood_index = lst_lines_f.index(esm) + 3
            tedad_vorood = int(lst_lines_f[tedad_vorood_index]) + 1
            tedad_bord_index = lst_lines_f.index(esm) + 1
            tedad_bord = int(lst_lines_f[tedad_bord_index])
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index])
            if tedad_vorood == 0:
                tedad_vorood = 0
                tedad_bord = 0
                tedad_bakht = 0

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_vorood_index] = tedad_vorood
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            email_guest = lst_lines_f[mail_index][:-1]

            print(f'Welcome back {name}\n')

            print(f'tedadvorood : {tedad_vorood}\n')
            print(f'tedadbakht : {tedad_bakht}\n')

            send_email_admin(name, tedad_vorood, tedad_bord, tedad_bakht)
        else:
            print(
                'You have entered wrong password or your name exist in databese (choose another name)\a')
            sys.exit()

    else:
        email_guest = input('Enter your email please : ')
        a = 0
        namepass1 = set({})
        password1 = input('Enter your game password please : ')
        namepass1.add((name, password1))
        tedad_vorood = 1
        tedad_bord = 0
        tedad_bakht = 0
        f.write(f'{name}\n')
        f.write(f'{tedad_bord}\n')
        f.write(f'{tedad_bakht}\n')
        f.write(f'{tedad_vorood}\n')
        f.write(f'namepass : {namepass1}\n')
        f.write(email_guest)
        f.write('\n---------------------------------------------\n')
        print(f'Welcome {name}\n')
        print(f'tedadvorood : {tedad_vorood}\n')
        send_email_admin(name, tedad_vorood, tedad_bord, tedad_bakht)

    if masahat_zamin == 300:
        masahat_timer = (1000, 520, 5)
    elif masahat_zamin == 144:
        masahat_timer = (900, 348, 50)
    else:
        masahat_timer = (800, 288, 100)

    master = Tk()
    master.geometry(
        f'{masahat_zamin+masahat_timer[0]}x{masahat_zamin+masahat_timer[1]}')
    master.title('Minesweeper')
    bomb_positions = []

    ico = Image.open('min.png')
    photo = ImageTk.PhotoImage(ico)
    master.wm_iconphoto(False, photo)

    bmb_index = []
    for k in range(10**3):
        bmb_index = list(bmb_index)
        bmb_index.append(randint(0, n*m))
        bmb_index = set(bmb_index)
        if len(bmb_index) == tedad_bomb:
            break
    bmb_index = list(bmb_index)

    flag_index = []

    def place_flag(square):
        global tedad_flag
        global tedad_bord
        print("PlaceFlag")
        tedad_flag -= 1
        print(f'You have {tedad_flag} flags \a')
        btnList[square]['text'] = u'\u2690'
        flag_index.append(square)
        if tedad_flag == 0:
            print('It was your last flag\a')
        if tedad_flag < 0:
            print('Error you used all your flags \a')
            master.destroy()

        s = 0

        for i in flag_index:
            if i in bomb_positions:
                s += 1
            if s == len(bomb_positions):
                print('Congratulation')
                print('You win\a')
                tedad_bord_index = lst_lines_f.index(esm) + 1
                tedad_bord = int(lst_lines_f[tedad_bord_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bord_index] = tedad_bord

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)
                ts.sleep(1)
                master.destroy()
                k = input(
                    '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
                if k == '2':
                    o = input(
                        'Are you sure? Do you want to exit?(yes or no) : \a')
                    o.lower()
                if k == "1":

                    Minesweeper()

                elif k == "2" and o == 'yes':
                    ts.sleep(1)

                    z = 0
                    for satr in range(m):
                        for sotoon in range(n):
                            if sotoon == n-1:
                                if z in bmb_index:
                                    print('✺')
                                else:
                                    print('☑')
                                z += 1
                            else:
                                if z in bmb_index:
                                    print('✺', end=' ')
                                else:
                                    print('☑', end=' ')
                                z += 1

                    print(list(map(lambda i: i+1, bomb_positions)))

                    quit()

    def check(square, btn):
        print("Check ", square, btn)
        if square in bomb_positions:
            print("Booommmmm!!!\a")

            btnList[square]['text'] = u'\u273A'
            messagebox.showinfo("Lose", " You lose")
            with open('database.txt', 'r') as f1:
                lst_lines_f = f1.readlines()

            # update tedad bakht
            # if tedad_vorood != 1:
                tedad_bakht_index = lst_lines_f.index(esm) + 2
                tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

                with open('database.txt', 'w') as f2:
                    lst_lines_f[tedad_bakht_index] = tedad_bakht

                    for i in lst_lines_f:
                        if type(i) == int:
                            i = str(i) + '\n'
                        f2.write(i)

            ts.sleep(1)
            master.destroy()
            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":

                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()

            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))

                quit()

        else:

            print(str(emtehan(square)))
            btnList[square]['text'] = str(emtehan(square))

    def setFocus(event):
        event.widget.focus_set()

    btnList = []

    for i in range(n*m):

        row, col = divmod(i, n)

        # btn = Button(master, width=4, height = 2)

        # btn.grid(row=row, column=col)

        if i not in bmb_index:  # These are 'safe' buttons
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))

            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))

            btn.grid(row=row, column=col)

        if i in bmb_index:  # These are 'bombs'
            btn = Button(master, width=4, height=2)
            btn.bind('<ButtonRelease-1>', lambda event, i=i: check(i, btn))
            btn.bind('<ButtonRelease-3>', lambda event, i=i: place_flag(i))
            btn.grid(row=row, column=col)
            bomb_positions.append(i)

        btnList.append(btn)
        btn.bind("<Enter>", setFocus)

    '''--------------------------------- Timer box --------------------------------'''
    time = 5 * masahat_zamin

    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    work_sec = time
    timer = None

    # ---------------------------- TIMER RESET ------------------------------- #

    def reset_timer():
        master.after_cancel(timer)
        canvas.itemconfig(timer_text, text=f'{time}')
        title_label.config(text="Timer")

        global reps
        reps = 0

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    def start_timer():
        global reps
        reps += 1
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    def count_down(count):

        count_sec = count

        canvas.itemconfig(timer_text, text=f"{count_sec}")
        if count > 0:
            global timer
            timer = master.after(1000, count_down, count - 1)
        else:
            messagebox.showinfo("Time countdown", "Time's Up = > You lose")
            print("Time's Up = > You lose\a")

            # update tedad bakht
            tedad_bakht_index = lst_lines_f.index(esm) + 2
            tedad_bakht = int(lst_lines_f[tedad_bakht_index]) + 1

            with open('database.txt', 'w') as f2:
                lst_lines_f[tedad_bakht_index] = tedad_bakht

                for i in lst_lines_f:
                    if type(i) == int:
                        i = str(i) + '\n'
                    f2.write(i)

            k = input(
                '''If you want play again enter 1  or  if you want see "bomb's positions and quit" enter 2 : ''')
            if k == '2':
                o = input('Are you sure? Do you want to exit?(yes or no) : \a')
                o.lower()
            if k == "1":
                Minesweeper()
            elif k == '2' and o == 'no':
                Minesweeper()
            elif k == "2" and o == 'yes':
                ts.sleep(1)

                z = 0
                for satr in range(m):
                    for sotoon in range(n):
                        if sotoon == n-1:
                            if z in bmb_index:
                                print('✺')
                            else:
                                print('☑')
                            z += 1
                        else:
                            if z in bmb_index:
                                print('✺', end=' ')
                            else:
                                print('☑', end=' ')
                            z += 1

                print(list(map(lambda i: i+1, bomb_positions)))
                quit()

    timer_in_zamin_1 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_2 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    timer_in_zamin_3 = {'start': (masahat_timer[0] - masahat_timer[2] - 100, masahat_timer[1]//2 + 150),
                        'reset': (masahat_timer[0] - masahat_timer[2] - 250, masahat_timer[1]//2 + 150),
                        'exit': (masahat_timer[0] - masahat_timer[2] - 152,  masahat_timer[1]//2 + 150)}

    start_button = Button(text="Start", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=start_timer)
    reset_button = Button(text="Reset", highlightthickness=0, bg="#F1583F", fg="#fff", font=(
        FONT_NAME, 15, "bold"), command=reset_timer)
    exit_button = Button(bg="#F1583F", fg="#fff", text="Exit", command=quit)

    if zamin_bazi == '1':
        ax_timer = (450, 20)

        start_button.place(
            x=timer_in_zamin_1['start'][0], y=timer_in_zamin_1['start'][1])

        reset_button.place(
            x=timer_in_zamin_1['reset'][0], y=timer_in_zamin_1['reset'][1])

        exit_button.place(
            x=timer_in_zamin_1['exit'][0], y=timer_in_zamin_1['exit'][1])

    if zamin_bazi == '2':
        ax_timer = (600, 65)

        start_button.place(
            x=timer_in_zamin_2['start'][0], y=timer_in_zamin_2['start'][1])

        reset_button.place(
            x=timer_in_zamin_2['reset'][0], y=timer_in_zamin_2['reset'][1])

        exit_button.place(
            x=timer_in_zamin_2['exit'][0], y=timer_in_zamin_2['exit'][1])

    if zamin_bazi == '3':
        ax_timer = (750, 150)

        start_button.place(
            x=timer_in_zamin_3['start'][0], y=timer_in_zamin_3['start'][1])

        reset_button.place(
            x=timer_in_zamin_3['reset'][0], y=timer_in_zamin_3['reset'][1])

        exit_button.place(
            x=timer_in_zamin_3['exit'][0], y=timer_in_zamin_3['exit'][1])

    # pause_button = Button(text="Pause", fg="#fff", bg="#F1583F")
    # pause_button.place(
    #     x=masahat_timer[0] - masahat_timer[2], y=masahat_timer[1]//2 + 200)
    # I couldn't find a command (algorithm) for pause btn so if you have an idea about it you can email me #

    # label
    title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
    title_label.place(x=masahat_timer[0] -
                      masahat_timer[2], y=masahat_timer[1]//2)

    # config UI for canvas
    canvas = Canvas(width=200, height=224,  highlightthickness=0)
    timer_img = PhotoImage(file="timer01.png")
    canvas.create_image(100, 112, image=timer_img)
    timer_text = canvas.create_text(
        100, 130, text=f"{time}", fill="blue", font=(FONT_NAME, 35, "bold"))
    canvas.place(x=ax_timer[0], y=ax_timer[1])

    master.mainloop()
>>>>>>> deba06a (BP Projects Added)
