'''
Hi, dear TA 

Now it's my turn!!!!  (:

Please solve this question; then email me with "mail code box" if you have any problem about this you can see this website : 
< https://www.roxo.ir/professional-python-sending-a-mail >


----------------------------------------------------------------------------------------------------------------------

Problem ==> Red Buttons from  IUT CPC 

 Masih is greatly interested in red buttons, so much so that he has invented a new game using
them. This game is played between two players, each of which has an infinite number of red
buttons. On each red button is a distinct string of letters, which we call the button’s Code. In
each turn, the rival will choose two buttons with n-letter Codes and give them to Masih (We call
these two strings A and B). He should find the button with the code A + B in the shortest time.
To do this, Masih takes the set of all strings of length n over a fixed alphabet. Then Masih sorts
all taken strings, thus obtaining a sorted sequence of strings T. Let’s denote the length of T as
M, and enumerate the elements of this sequence as T0, T1, . . . TM−1. Now Masih says that the
sum of two strings A = Ta and B = Tb is a string C = Tc where c = (a + b) mod M.
Masih has no interest in losing, so you should help Masih find the sum of two given strings A
and B over the alphabet of small English letters.

Input :
     The input file consists of two lines containing strings A and B of the same length. Both strings
    consist of small letters of English alphabet. The length of each string doesn’t exceed 100000 .


    A = gahjeeabhedaay
    B = galzdpamhqosab

output :
    Output is I

Example 1 :
    A = kak
    B = sam
    I = caw

Example 2 :
    A = z
    B = y
    I = x


----------------------------------------------------------------------------------------------------------------------

 
You need < 'I' > to send me an email so be carful < 'I' > is main body of my email !!
I'll send the project to you by email after viewing your email.

|||||| NOTICE :
    for using gmail server, at first you should turn on 'Less Secured Apps' from your gmail account setting ||||||
    < https://www.roxo.ir/professional-python-sending-a-mail >




If I have any problem in my writing forgive me. :()

written by Masih Tanoursaz

Good  luck
'''
# I tried this code for mine (gmail not else) and fortunately it worked .


# <<< mail code box >>>
# ----------------------------------------------------------------------------------------

import smtplib
from email.message import EmailMessage



email = EmailMessage()

email['from'] = input('Enter your email please : ')

efrom = email['from']

password = input('Enter your email pass : ')

email['to'] = input('Enter my email : my email is: I@gmail.com :: ' )

email['subject'] = 'Hello, the problem has been solved'



email.set_content('Send your game code please')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try :
        smtp.ehlo()

        smtp.starttls()

        smtp.login(efrom, password)

        smtp.send_message(email)

        

        print('email was sent!')
    except :
        print("email wasn't sent!")
# ----------------------------------------------------------------------------------------

# It was just an attempt to test my self 

# << I hope you like it >>