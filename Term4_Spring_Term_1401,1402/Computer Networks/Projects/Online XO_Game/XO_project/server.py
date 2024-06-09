import pickle
import socket
import threading
import tkinter as tk
from time import sleep

# get the hostname
hostname = socket.gethostname()
# get the IP address
HOST_ADDR = socket.gethostbyname(hostname)
HOST_PORT = 12345
connectedClients = []
clientsName = []
# print the IP address
print(f"Server IP address is: {HOST_ADDR}")

# create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a port
mysock.bind((HOST_ADDR, HOST_PORT))

# create a GUI window using tkinter
window = tk.Tk()
window.title("Tic-Tac-Toe Server")
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
window.configure(background='#2C3333')

# function to start the server and accept clients


def start_server():
    try:
        # listen for incoming connections
        mysock.listen()
        listening = mysock.getsockopt(socket.SOL_SOCKET, socket.SO_ACCEPTCONN)
        print('Server is listening....')
        if listening:
            btnStart.config(state=tk.DISABLED)
            lblStatus.config(text='ONLINE', fg='green', bg='#2C3333')
            lblHost["text"] = "Address: " + HOST_ADDR
            lblPort["text"] = "Port: " + str(HOST_PORT)
            btnStart.config(state=tk.DISABLED)

        threading._start_new_thread(accept_clients, (mysock, " "))
    except socket.error as e:
        print(f"Error starting server: {e}")


def start_server_bind_return(event):
    start_server()


# bind the 'Enter' key to the start_server function
window.bind('<Return>', start_server_bind_return)


# function to accept incoming client connections
def accept_clients(the_server, y):
    while True:
        try:
            # accept the connection from the client
            client, addr = the_server.accept()
            connectedClients.append(client)
            # use a thread to handle the communication with the client
            threading._start_new_thread(
                send_receive_client_message, (client, addr))
        except socket.error as e:
            print(f"Error accepting client: {e}")

# function to update the client names display when a new client connects or a client disconnects


def update_client_names_display(name_list):
    tkDisplay.config(state=tk.NORMAL)
    tkDisplay.delete('1.0', tk.END)

    for c in name_list:
        tkDisplay.insert(tk.END, '\u2022 '+c+"\n")
        tkDisplay.tag_configure("bullet", foreground="green")
        tkDisplay.tag_add("bullet", "1.0", "1.1")

    tkDisplay.config(state=tk.DISABLED)


# function to receive messages from the client and send specific response to it
def send_receive_client_message(client_connection, client_ip_addr):
    try:
        # send welcome message to client and get client name
        client_connection.sendall('welcome'.encode())
        client_name = client_connection.recv(4096).decode()
        clientsName.append(client_name)
        update_client_names_display(clientsName)

        while True:
            data = client_connection.recv(4096).decode()
            if not data:
                break
            # send the client list to a client requesting it
            if data.startswith("getlist"):
                mapped_list = list(zip([i.getpeername()
                                        for i in connectedClients], clientsName))
                for c in connectedClients:
                    c.sendall(pickle.dumps(mapped_list))

    except (ConnectionResetError, socket.error):
        # client lost connection
        connectedClients.remove(client_connection)
        clientsName.remove(client_name)
        update_client_names_display(clientsName)


# create the GUI elements
topFrame = tk.Frame(window)
topFrame.configure(background='#2C3333')
btnStart = tk.Button(topFrame, text="Start", command=start_server)
btnStart.configure(background='#AAFF00')
btnStart.pack(side=tk.LEFT)
topFrame.pack(side=tk.TOP, pady=(5, 0))


# Middle frame consisting of two labels for displaying the host and port info
middleFrame = tk.Frame(window)
middleFrame.configure(background='#2C3333')
lblHost = tk.Label(middleFrame, text="Address:X.X.X.X")
lblHost.config(bg='#2C3333', fg='#CBE4DE')
lblHost.pack(side=tk.LEFT)
lblPort = tk.Label(middleFrame, text="Port:XXXX")
lblPort.config(bg='#2C3333', fg='#CBE4DE')
lblPort.pack(side=tk.LEFT)
middleFrame.pack(side=tk.TOP, pady=(5, 0))

# Define a function to copy lblHost value to clipboard


def copy_to_clipboard():
    window.clipboard_clear()
    ip_copy = lblHost['text'].replace('Address: ', '')
    window.clipboard_append(ip_copy)
    window.update()


# create a PhotoImage object
img = tk.PhotoImage(file="XO_project\copy_icon.png")
# Create a button and pack it on the right side of the middleFrame
btnCopy = tk.Button(middleFrame, image=img, command=copy_to_clipboard)
btnCopy.config(bg='#2C3333')
btnCopy.pack(side=tk.RIGHT)

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
                 highlightbackground="gray", state="disable", fg='#CBE4DE')
clientFrame.pack(side=tk.TOP, pady=(5, 5))


# The status frame for showing the status of server
statusFrame = tk.Frame(window)
lblStatus = tk.Label(statusFrame, text="OFFLINE")
lblStatus.config(bg='red')
statusFrame.config(bg='#2C3333')
lblStatus.pack()
statusFrame.pack(side=tk.BOTTOM)

window.mainloop()


print(connectedClients)
