# def init(arg0, arg1):
#     global list_labels, your_turn, your_details, opponent_details, you_started

#     sleep(3)

#     for i in range(len(list_labels)):
#         list_labels[i]["symbol"] = ""
#         list_labels[i]["ticked"] = False
#         list_labels[i]["label"]["text"] = ""
#         list_labels[i]["label"].config(foreground="black", highlightbackground="grey",
#                                        highlightcolor="grey", highlightthickness=1)

#     lbl_status.config(foreground="black")
#     lbl_status["text"] = "STATUS: Game's starting."
#     sleep(1)
#     lbl_status["text"] = "STATUS: Game's starting.."
#     sleep(1)
#     lbl_status["text"] = "STATUS: Game's starting..."
#     sleep(1)

#     if you_started:
#         you_started = False
#         your_turn = False
#         lbl_status["text"] = "STATUS: " + opponent_details["name"] + "'s turn!"
#     else:
#         you_started = True
#         your_turn = True
#         lbl_status["text"] = "STATUS: Your turn!"


# def get_cordinate(xy):
#     global client, your_turn
#     # convert 2D to 1D cordinate i.e. index = x * num_cols + y
#     label_index = xy[0] * num_cols + xy[1]
#     label = list_labels[label_index]

#     if your_turn:
#         if label["ticked"] is False:
#             label["label"].config(foreground=your_details["color"])
#             label["label"]["text"] = your_details["symbol"]
#             label["ticked"] = True
#             label["symbol"] = your_details["symbol"]
#             # send xy cordinate to server
#             client.send(("$xy$" + str(xy[0]) + "$" + str(xy[1])).encode())
#             your_turn = False

#             # Does this play leads to a win or a draw
#             result = game_logic()
#             if result[0] is True and result[1] != "":  # a win
#                 your_details["score"] = your_details["score"] + 1
#                 lbl_status["text"] = "Game over, You won! You(" + str(your_details["score"]) + ") - " \
#                     "" + opponent_details["name"] + \
#                     "(" + str(opponent_details["score"])+")"
#                 lbl_status.config(foreground="green")
#                 threading._start_new_thread(init, ("", ""))

#             elif result[0] is True and result[1] == "":  # a draw
#                 lbl_status["text"] = "Game over, Draw! You(" + str(your_details["score"]) + ") - " \
#                     "" + opponent_details["name"] + \
#                     "(" + str(opponent_details["score"]) + ")"
#                 lbl_status.config(foreground="blue")
#                 threading._start_new_thread(init, ("", ""))

#             else:
#                 lbl_status["text"] = "STATUS: " + \
#                     opponent_details["name"] + "'s turn!"
#     else:
#         lbl_status["text"] = "STATUS: Wait for your turn!"
#         lbl_status.config(foreground="red")


# # [(0,0) -> (0,1) -> (0,2)], [(1,0) -> (1,1) -> (1,2)], [(2,0), (2,1), (2,2)]
# def check_row():
#     list_symbols = []
#     list_labels_temp = []
#     winner = False
#     win_symbol = ""
#     for i in range(len(list_labels)):
#         list_symbols.append(list_labels[i]["symbol"])
#         list_labels_temp.append(list_labels[i])
#         if (i + 1) % 3 == 0:
#             if (list_symbols[0] == list_symbols[1] == list_symbols[2]):
#                 if list_symbols[0] != "":
#                     winner = True
#                     win_symbol = list_symbols[0]

#                     list_labels_temp[0]["label"].config(foreground="green", highlightbackground="green",
#                                                         highlightcolor="green", highlightthickness=2)
#                     list_labels_temp[1]["label"].config(foreground="green", highlightbackground="green",
#                                                         highlightcolor="green", highlightthickness=2)
#                     list_labels_temp[2]["label"].config(foreground="green", highlightbackground="green",
#                                                         highlightcolor="green", highlightthickness=2)

#             list_symbols = []
#             list_labels_temp = []

#     return [winner, win_symbol]


# # [(0,0) -> (1,0) -> (2,0)], [(0,1) -> (1,1) -> (2,1)], [(0,2), (1,2), (2,2)]
# def check_col():
#     winner = False
#     win_symbol = ""
#     for i in range(num_cols):
#         if list_labels[i]["symbol"] == list_labels[i + num_cols]["symbol"] == list_labels[i + num_cols + num_cols][
#                 "symbol"]:
#             if list_labels[i]["symbol"] != "":
#                 winner = True
#                 win_symbol = list_labels[i]["symbol"]

#                 list_labels[i]["label"].config(foreground="green", highlightbackground="green",
#                                                highlightcolor="green", highlightthickness=2)
#                 list_labels[i + num_cols]["label"].config(foreground="green", highlightbackground="green",
#                                                           highlightcolor="green", highlightthickness=2)
#                 list_labels[i + num_cols + num_cols]["label"].config(foreground="green", highlightbackground="green",
#                                                                      highlightcolor="green", highlightthickness=2)

#     return [winner, win_symbol]


# def check_diagonal():
#     winner = False
#     win_symbol = ""
#     i = 0
#     j = 2

#     # top-left to bottom-right diagonal (0, 0) -> (1,1) -> (2, 2)
#     a = list_labels[i]["symbol"]
#     b = list_labels[i + (num_cols + 1)]["symbol"]
#     c = list_labels[(num_cols + num_cols) + (i + 1)]["symbol"]
#     if list_labels[i]["symbol"] == list_labels[i + (num_cols + 1)]["symbol"] == \
#             list_labels[(num_cols + num_cols) + (i + 2)]["symbol"]:
#         if list_labels[i]["symbol"] != "":
#             winner = True
#             win_symbol = list_labels[i]["symbol"]

#             list_labels[i]["label"].config(foreground="green", highlightbackground="green",
#                                            highlightcolor="green", highlightthickness=2)

#             list_labels[i + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
#                                                             highlightcolor="green", highlightthickness=2)
#             list_labels[(num_cols + num_cols) + (i + 2)]["label"].config(foreground="green",
#                                                                          highlightbackground="green",
#                                                                          highlightcolor="green", highlightthickness=2)

#     # top-right to bottom-left diagonal (0, 0) -> (1,1) -> (2, 2)
#     elif list_labels[j]["symbol"] == list_labels[j + (num_cols - 1)]["symbol"] == list_labels[j + (num_cols + 1)][
#             "symbol"]:
#         if list_labels[j]["symbol"] != "":
#             winner = True
#             win_symbol = list_labels[j]["symbol"]

#             list_labels[j]["label"].config(foreground="green", highlightbackground="green",
#                                            highlightcolor="green", highlightthickness=2)
#             list_labels[j + (num_cols - 1)]["label"].config(foreground="green", highlightbackground="green",
#                                                             highlightcolor="green", highlightthickness=2)
#             list_labels[j + (num_cols + 1)]["label"].config(foreground="green", highlightbackground="green",
#                                                             highlightcolor="green", highlightthickness=2)
#     else:
#         winner = False

#     return [winner, win_symbol]


# # it's a draw if grid is filled
# def check_draw():
#     for i in range(len(list_labels)):
#         if list_labels[i]["ticked"] is False:
#             return [False, ""]
#     return [True, ""]


# def game_logic():
#     result = check_row()
#     if result[0]:
#         return result

#     result = check_col()
#     if result[0]:
#         return result

#     result = check_diagonal()
#     if result[0]:
#         return result

#     result = check_draw()
#     return result
