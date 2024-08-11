import pickle
import socket
import threading
import tkinter as tk
from time import sleep
from tkinter import messagebox

# network client for sever tranactions
HOST_ADDR = None
HOST_PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connectedClients = []
clientsName = []

# network client for comunication with other clients
i_am_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
i_am_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


list_labels = []
num_cols = 3
your_turn = False
you_started = False
i_am_client = True

my_details = {
    "name": "masih",
    "symbol": "O",
    "color": "red",
    "score": 0,
    'ip': '',
    'port': ''
}

opponent_details = {
    "name": "",
    "symbol": "X",
    "color": "orange",
    "score": 0,
    'ip': '',
    'port': ''
}


def clear_window(root):
    for widget in root.winfo_children():
        widget.destroy()


def start_game(window_main):
    global my_details, opponent_details, your_turn, you_started, i_am_client_socket, i_am_server_socke
    print('in start game')
    print('my', my_details)
    print('opponent', opponent_details)
    clear_window(window_main)
    top_frame = tk.Frame(window_main)
    # Create Table 3x3 for xo game
    for x in range(3):
        for y in range(3):
            lbl = tk.Label(top_frame, text=" ", font="Helvetica 45 bold", height=2, width=5, highlightbackground="grey",
                           highlightcolor="grey", highlightthickness=1)
            lbl.bind("<Button-1>", lambda e, xy=[x, y]: get_cordinate(xy))
            lbl.grid(row=x, column=y)

        dict_labels = {"xy": [x, y], "symbol": "",
                       "label": lbl, "ticked": False}
        list_labels.append(dict_labels)

    lbl_status = tk.Label(
        top_frame, text="Status: Not connected to server", font="Helvetica 14 bold")
    lbl_status.grid(row=3, columnspan=3)

    top_frame.pack()

    def init(arg0, arg1):
        global list_labels, your_turn, my_details, opponent_details, you_started

        sleep(3)

        for i in range(len(list_labels)):
            list_labels[i]["symbol"] = ""
            list_labels[i]["ticked"] = False
            list_labels[i]["label"]["text"] = ""
            list_labels[i]["label"].config(foreground="black", highlightbackground="grey",
                                           highlightcolor="grey", highlightthickness=1)

        lbl_status.config(foreground="black")
        lbl_status["text"] = "STATUS: Game's starting."
        sleep(1)
        lbl_status["text"] = "STATUS: Game's starting.."
        sleep(1)
        lbl_status["text"] = "STATUS: Game's starting..."
        sleep(1)

        if you_started:
            you_started = False
            your_turn = False
            lbl_status["text"] = "STATUS: " + \
                opponent_details["name"] + "'s turn!"
        else:
            you_started = True
            your_turn = True
            lbl_status["text"] = "STATUS: Your turn!"

    def get_cordinate(xy):
        global client, your_turn
        # convert 2D to 1D cordinate i.e. index = x * num_cols + y
        label_index = xy[0] * num_cols + xy[1]
        label = list_labels[label_index]

        if your_turn:
            if label["ticked"] is False:
                label["label"].config(foreground=my_details["color"])
                label["label"]["text"] = my_details["symbol"]
                label["ticked"] = True
                label["symbol"] = my_details["symbol"]
                # send xy cordinate to server
                client.send(("$xy$" + str(xy[0]) + "$" + str(xy[1])).encode())
                your_turn = False

                # Does this play leads to a win or a draw
                result = game_logic()
                if result[0] is True and result[1] != "":  # a win
                    my_details["score"] = my_details["score"] + 1
                    lbl_status["text"] = "Game over, You won! You(" + str(my_details["score"]) + ") - " \
                        "" + opponent_details["name"] + \
                        "(" + str(opponent_details["score"])+")"
                    lbl_status.config(foreground="green")
                    threading._start_new_thread(init, ("", ""))

                elif result[0] is True and result[1] == "":  # a draw
                    lbl_status["text"] = "Game over, Draw! You(" + str(my_details["score"]) + ") - " \
                        "" + opponent_details["name"] + \
                        "(" + str(opponent_details["score"]) + ")"
                    lbl_status.config(foreground="blue")
                    threading._start_new_thread(init, ("", ""))

                else:
                    lbl_status["text"] = "STATUS: " + \
                        opponent_details["name"] + "'s turn!"
        else:
            lbl_status["text"] = "STATUS: Wait for your turn!"
            lbl_status.config(foreground="red")

            # send xy coordinate to server to server

    # [(0,0) -> (0,1) -> (0,2)], [(1,0) -> (1,1) -> (1,2)], [(2,0), (2,1), (2,2)]
    def check_row():
        list_symbols = []
        list_labels_temp = []
        winner = False
        win_symbol = ""
        for i in range(len(list_labels)):
            list_symbols.append(list_labels[i]["symbol"])
            list_labels_temp.append(list_labels[i])
            if (i + 1) % 3 == 0:
                if (list_symbols[0] == list_symbols[1] == list_symbols[2]):
                    if list_symbols[0] != "":
                        winner = True
                        win_symbol = list_symbols[0]

                        list_labels_temp[0]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)
                        list_labels_temp[1]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)
                        list_labels_temp[2]["label"].config(foreground="green", highlightbackground="green",
                                                            highlightcolor="green", highlightthickness=2)

                list_symbols = []
                list_labels_temp = []

        return [winner, win_symbol]

    # [(0,0) -> (1,0) -> (2,0)], [(0,1) -> (1,1) -> (2,1)], [(0,2), (1,2), (2,2)]

    def check_col():
        winner = False
        win_symbol = ""
        for i in range(num_cols):
            if list_labels[i]["symbol"] == list_labels[i + num_cols]["symbol"] == list_labels[i + num_cols + num_cols][
                    "symbol"]:
                if list_labels[i]["symbol"] != "":
                    winner = True
                    win_symbol = list_labels[i]["symbol"]

                    list_labels[i]["label"].config(foreground="green", highlightbackground="green",
                                                   highlightcolor="green", highlightthickness=2)
                    list_labels[i + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                              highlightcolor="green", highlightthickness=2)
                    list_labels[i + num_cols + num_cols]["label"].config(foreground="green", highlightbackground="green",
                                                                         highlightcolor="green", highlightthickness=2)

        return [winner, win_symbol]

    def check_diagonal():
        winner = False
        win_symbol = ""
        i = 0
        j = 2

        # top-left to bottom-right diagonal (0, 0) -> (1,1) -> (2, 2)
        a = list_labels[i]["symbol"]
        b = list_labels[i + (num_cols + 1)]["symbol"]
        c = list_labels[(num_cols + num_cols) + (i + 1)]["symbol"]
        if list_labels[i]["symbol"] == list_labels[i + (num_cols + 1)]["symbol"] == \
                list_labels[(num_cols + num_cols) + (i + 2)]["symbol"]:
            if list_labels[i]["symbol"] != "":
                winner = True
                win_symbol = list_labels[i]["symbol"]

                list_labels[i]["label"].config(foreground="green", highlightbackground="green",
                                               highlightcolor="green", highlightthickness=2)

                list_labels[i + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
                                                                highlightcolor="green", highlightthickness=2)
                list_labels[(num_cols + num_cols) + (i + 2)]["label"].config(foreground="green",
                                                                             highlightbackground="green",
                                                                             highlightcolor="green", highlightthickness=2)

        # top-right to bottom-left diagonal (0, 0) -> (1,1) -> (2, 2)
        elif list_labels[j]["symbol"] == list_labels[j + (num_cols - 1)]["symbol"] == list_labels[j + (num_cols + 1)][
                "symbol"]:
            if list_labels[j]["symbol"] != "":
                winner = True
                win_symbol = list_labels[j]["symbol"]

                list_labels[j]["label"].config(foreground="green", highlightbackground="green",
                                               highlightcolor="green", highlightthickness=2)
                list_labels[j + (num_cols - 1)]["label"].config(foreground="green", highlightbackground="green",
                                                                highlightcolor="green", highlightthickness=2)
                list_labels[j + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
                                                                highlightcolor="green", highlightthickness=2)
        else:
            winner = False

        return [winner, win_symbol]

    # it's a draw if grid is filled

    def check_draw():
        for i in range(len(list_labels)):
            if list_labels[i]["ticked"] is False:
                return [False, ""]
        return [True, ""]

    def game_logic():
        result = check_row()
        if result[0]:
            return result

        result = check_col()
        if result[0]:
            return result

        result = check_diagonal()
        if result[0]:
            return result

        result = check_draw()
        return result

    def receive_message_from_other_client(sck, m):
        global my_details, opponent_details, your_turn, you_started
        while True:
            from_server = sck.recv(4096).decode()
            print(from_server)
            if my_details["symbol"] == "O":
                lbl_status["text"] = "STATUS: Your turn!"
                your_turn = True
                you_started = True
            else:
                lbl_status["text"] = "STATUS: " + \
                    opponent_details["name"] + "'s turn!"
                you_started = False
                your_turn = False

            if not from_server:
                break

            # if from_server.startswith("welcome"):
            #     if from_server == "welcome1":
            #         my_details["color"] = "purple"
            #         opponent_details["color"] = "orange"
            #         lbl_status["text"] = "Server: Welcome " + \
            #             my_details["name"] + "! Waiting for player 2"
            #     elif from_server == "welcome2":
            #         lbl_status["text"] = "Server: Welcome " + \
            #             my_details["name"] + "! Game will start soon"
            #         my_details["color"] = "orange"
            #         opponent_details["color"] = "purple"

            # elif from_server.startswith("opponent_name$"):
            #     temp = from_server.replace("opponent_name$", "")
            #     temp = temp.replace("symbol", "")
            #     name_index = temp.find("$")
            #     symbol_index = temp.rfind("$")
            #     opponent_details["name"] = temp[0:name_index]
            #     my_details["symbol"] = temp[symbol_index:len(temp)]

            #     # set opponent symbol
            #     if my_details["symbol"] == "O":
            #         opponent_details["symbol"] = "X"
            #     else:
            #         opponent_details["symbol"] = "O"

            #     lbl_status["text"] = "STATUS: " + \
            #         opponent_details["name"] + " is connected!"
            #     sleep(3)
            #     # is it your turn to play? hey! 'O' comes before 'X'
            elif from_server.startswith("$xy$"):
                temp = from_server.replace("$xy$", "")
                _x = temp[0:temp.find("$")]
                _y = temp[temp.find("$") + 1:len(temp)]

                # update board
                label_index = int(_x) * num_cols + int(_y)
                label = list_labels[label_index]
                label["symbol"] = opponent_details["symbol"]
                label["label"]["text"] = opponent_details["symbol"]
                label["label"].config(foreground=opponent_details["color"])
                label["ticked"] = True

                # Does this cordinate leads to a win or a draw
                result = game_logic()
                if result[0] is True and result[1] != "":  # opponent win
                    opponent_details["score"] = opponent_details["score"] + 1
                    if result[1] == opponent_details["symbol"]:  #
                        lbl_status["text"] = "Game over, You Lost! You(" + str(my_details["score"]) + ") - " \
                            "" + opponent_details["name"] + \
                            "(" + str(opponent_details["score"]) + ")"
                        lbl_status.config(foreground="red")
                        threading._start_new_thread(init, ("", ""))
                elif result[0] is True and result[1] == "":  # a draw
                    lbl_status["text"] = "Game over, Draw! You(" + str(my_details["score"]) + ") - " \
                        "" + opponent_details["name"] + \
                        "(" + str(opponent_details["score"]) + ")"
                    lbl_status.config(foreground="blue")
                    threading._start_new_thread(init, ("", ""))
                else:
                    your_turn = True
                    lbl_status["text"] = "STATUS: Your turn!"
                    lbl_status.config(foreground="black")

        sck.close()

    if my_details["symbol"] == 'O':
        print('in client side')
        threading._start_new_thread(
            receive_message_from_other_client, (i_am_client_socket, "m"))
    else:
        print('in server side')
        threading._start_new_thread(
            receive_message_from_other_client, (i_am_server_socket, "m"))


def startSecondUi():
    # clear_window(window)
    global clientsName, connectedClients, my_details, opponent_details, i_am_client, your_turn, you_started

    def start_listening_for_other_client():
        try:
            # listen for incoming connections
            i_am_server_socket.bind((my_details['ip'], my_details['port']))
            i_am_server_socket.listen(1)
            print('Server thread started...',
                  my_details['ip'], my_details['port'])
            otherclient, otherclientaddrs = i_am_server_socket.accept()
            request = otherclient.recv(4096).decode()
            if request.startswith('Do You want play XO'):
                answer = tk.messagebox.askquestion(
                    "Confirmation", request)
                otherclient.sendall(answer.encode())
                if answer == 'yes':
                    # get opponent name
                    print(otherclientaddrs)
                    opponent_details["name"] = otherclient.recv(4096).decode()
                    opponent_details["ip"] = otherclientaddrs[0]
                    opponent_details["port"] = otherclientaddrs[1]-1
                    my_details["symbol"] == "X"
                    opponent_details["symbol"] = "O"
                    print('in listening as a server opponent is', opponent_details)
                    print('in listening as a server my is', my_details)
                    server_thread.join()
                    # Should starts game from here
                    start_game(window)
        except socket.error as e:
            print(f"Error starting server: {e}")

    # Initialize a thread for server and listening
    server_thread = threading.Thread(target=start_listening_for_other_client)
    global client

    window = tk.Tk()
    window.title("Tic-Tac-Toe client")
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.configure(background='#2C3333')

    # Top frame consisting of one button (Update) and two labels (Hint, Host)
    topFrame = tk.Frame(window)
    topFrame.configure(background='#2C3333')
    hintLbl = tk.Label(
        topFrame, text="*** Hint ***\nEnter the desired player's name, then press connect!", background='#2C3333', foreground='#CBE4DE')
    hintLbl.pack(side=tk.TOP)
    lblHost = tk.Label(
        topFrame, text="Your Address: X.X.X.X : XXXX")
    lblHost.configure(foreground='#CBE4DE', background='#2C3333')
    lblHost.pack(side=tk.LEFT)

    def update_client_names_display():
        global clientsName, connectedClients
        client.sendall('getlist'.encode())
        while True:
            from_server = client.recv(4096)
            if not from_server:
                break
            connectedClients, clientsName = list(
                zip(*pickle.loads(from_server)))
            tkDisplay.config(state=tk.NORMAL)
            tkDisplay.delete('1.0', tk.END)
            for c in clientsName:
                index = clientsName.index(c)
                ip_and_port = connectedClients[index][0] + ' : ' + \
                    str(connectedClients[index][1])
                if c == my_details["name"]:
                    my_details['ip'] = connectedClients[index][0]
                    my_details['port'] = connectedClients[index][1]
                    window.title(my_details['name'])
                    lblHost.configure(
                        text="Your Address: {}".format(ip_and_port))
                    # Starts server thread from here
                    if not server_thread.is_alive():
                        server_thread.start()
                    continue
                tkDisplay.insert(tk.END, '\u2022 '+c +
                                 ' {}'.format(ip_and_port)+"\n")
            tkDisplay.config(state=tk.DISABLED)

        # window.after(1000, update_client_names_display)  # modified line

    # if connect btn pushed, we send a request to selcted client and get its response, if it was yes we start game otherwise close the connection.
    def connect_to_another_client():
        global your_turn, you_started, my_details, opponent_details
        if len(ent_name.get()) < 1:
            tk.messagebox.showerror(
                title="ERROR!!!", message="You MUST enter the first name of player that you want play with")
        else:
            flg_find = False
            for c in clientsName:
                if c == ent_name.get():
                    index = clientsName.index(c)
                    opponent_ip = connectedClients[index][0]
                    opponent_port = int(connectedClients[index][1])
                    flg_find = True
                    break
            if flg_find:
                i_am_client_socket.connect((opponent_ip, opponent_port))
                i_am_client_socket.sendall(
                    ('Do You want play XO with {} -> {}?'.format(my_details['name'], my_details['ip'])).encode())
                print('message was sent')
                response_to_play = i_am_client_socket.recv(4096).decode()
                if response_to_play == 'yes':
                    print('Should starts game')
                    # Send my name to the other client
                    i_am_client_socket.sendall(my_details['name'].encode())
                    # Game starts from here
                    opponent_details['name'] = ent_name.get()
                    opponent_details["ip"] = opponent_ip
                    opponent_details["port"] = opponent_port
                    opponent_details["symbol"] = "X"
                    you_started = True
                    your_turn = True
                    print('Opponent is ', opponent_details)
                    print('i am client', my_details)
                    start_game(window)

    btnUpdate = tk.Button(topFrame, text="Update Display", background='#CBE4DE',
                          command=update_client_names_display)

    btnUpdate.pack(side=tk.LEFT, pady=(5, 5), padx=(15, 0))
    topFrame.pack(side=tk.TOP, pady=(5, 0), padx=(8, 8))

    # The client frame shows the client list
    clientFrame = tk.Frame(window)
    clientFrame.configure(background='#2E4F4F')
    lblLine = tk.Label(clientFrame, text="**********Client List**********")
    lblLine.configure(foreground='#CBE4DE', background='#2E4F4F')
    lblLine.pack()
    scrollBar = tk.Scrollbar(clientFrame)
    scrollBar.pack(side=tk.RIGHT, fill=tk.Y)
    tkDisplay = tk.Text(clientFrame, height=10, width=30)
    tkDisplay.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
    scrollBar.config(command=tkDisplay.yview)
    tkDisplay.config(yscrollcommand=scrollBar.set, background="#2C3333",
                     highlightbackground="yellow", state="disable", fg='#CBE4DE')
    clientFrame.pack(side=tk.TOP, pady=(5, 5))

    # Bottom frame consisting of connect button, name lablel and name entry
    bottomFrame = tk.Frame(window)
    bottomFrame.pack(side=tk.BOTTOM)
    bottomFrame.configure(background='#2C3333')
    lbl_name = tk.Label(bottomFrame, text="Name:", background='#CBE4DE')
    ent_name = tk.Entry(bottomFrame, background='#CBE4DE')
    # Send a game request to server for that client
    connectBtn = tk.Button(bottomFrame, text="Connect", background="green",
                           command=connect_to_another_client)
    lbl_name.pack(side='left')
    ent_name.pack(side='left', padx=(6, 6))
    connectBtn.pack(side=tk.TOP, pady=(5, 5), padx=(10, 10))

    my_thread = threading.Thread(
        target=update_client_names_display)
    my_thread.start()

    print(client)
    # client.sendall('getlist'.encode())

    window.mainloop()


def startFirstUi():
    def connectToserver(name):
        global client, HOST_PORT, HOST_ADDR
        try:
            client.send(name.encode())  # Send name to server after connecting
            print('in connect to server')
            # start a thread to keep receiving message from server
            # do not block the main thread :)
            threading._start_new_thread(
                receive_message_from_server, (client, "m"))
        except Exception as e:
            tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(
                HOST_PORT) + " Server may be Unavailable. Try again later")

    def connect():
        global my_details
        if len(ent_name.get()) < 1:
            tk.messagebox.showerror(
                title="ERROR!!!", message="You MUST enter your first name <e.g. Masih>")
        else:
            my_details["name"] = ent_name.get()
            HOST_ADDR = ServerIP_entry.get()
            HOST_PORT = int(serverPort_entry.get())
            client.connect((HOST_ADDR, HOST_PORT))
            connectToserver(ent_name.get())

    def receive_message_from_server(sck, m):
        print('in recv')
        while True:
            from_server = sck.recv(4096).decode()
            print(from_server)
            print(client.getsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE))

            if not from_server:
                break

            if from_server.startswith("welcome"):
                window.iconify()
                # my_details['ip'] = sck.getpeername()[0]
                # my_details['port'] = sck.getpeername()[1]
                # print('in welcome', my_details)
                # server_thread.start()
                startSecondUi()

    window = tk.Tk()
    window.title("Tic-Tac-Toe Client")
    window.eval('tk::PlaceWindow . center')
    window.resizable(False, False)
    window.configure(background='#2C3333')

    # Server frame for getting ip address from client
    serverFrame = tk.Frame(window, background='#2C3333')
    serverFrame.pack()
    serverIP_lbl = tk.Label(window, background='#CBE4DE',
                            text='Server IP:')
    ServerIP_entry = tk.Entry(window)
    serverPort_lbl = tk.Label(window, background='#CBE4DE',
                              text='Server Port:')
    serverPort_entry = tk.Entry(window)
    serverPort_entry.insert(0, '12345')
    serverIP_lbl.pack(side='left', padx=5, pady=5)
    ServerIP_entry.pack(side='left', padx=5, pady=5)
    ServerIP_entry.focus_set()
    serverPort_lbl.pack(side='left', padx=5, pady=5)
    serverPort_entry.pack(side='left', padx=5, pady=5)
    serverFrame.pack(side='top')

    nameFrame = tk.Frame(window, background='#2C3333')
    nameFrame.pack()
    lbl_name = tk.Label(nameFrame, text="Name:", background='#CBE4DE')
    ent_name = tk.Entry(nameFrame, background='#CBE4DE')
    # Connect to server
    connectToServerBtn = tk.Button(nameFrame, text="Connect To Server", background="green",
                                   command=lambda: connect())
    lbl_name.pack(side='left')
    ent_name.pack(side='left', padx=(6, 6))
    connectToServerBtn.pack(side=tk.BOTTOM, pady=(5, 5), padx=(10, 10))

    window.mainloop()


startFirstUi()
