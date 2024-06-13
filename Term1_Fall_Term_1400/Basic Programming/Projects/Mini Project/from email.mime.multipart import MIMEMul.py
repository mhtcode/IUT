import smtplib
from email.message import EmailMessage



email = EmailMessage()

email['from'] = input('Enter your email please : ')

efrom = email['from']

password = input('Enter your email pass : ')

email['to'] = input('Enter my email : my email is:I+@gmail.com :: ' )

email['subject'] = 'Hello, the problem has been solved'



email.set_content('Send your game code please')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:

    smtp.ehlo()

    smtp.starttls()

    smtp.login(efrom, password)

    smtp.send_message(email)

    

    print('email was sent!')