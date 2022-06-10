import smtplib

name = input("Enter your Name/Company name")
sender = input("Enter your email address (Sender)")
password = input("Enter your password")
smtp_address = input("Enter SMTP address")
smtp_port = int(input("Enter SMTP port"))
heading = input("Enter Subject")
body = input("Enter your Message")
server = smtplib.SMTP(smtp_address, smtp_port)
server.starttls()

try:
    server.login(sender, password)
except smtplib.SMTPAuthenticationError:
    print("There is an error with your login details")
else:
    print("You have been successfully logged in!")


def send(add):
    message_format = f""""
    From: {name.upper()} \n
    To: {add} \n
    Subject: {heading.upper()} \n
    {body} \n\n
    Kind regards,
    The {name.upper()} Team
    """
    server.sendmail(sender, add, message_format)
    print(f"Your mail to {add} has been successfully sent!")


with open("addresses.txt", "r") as ad:
    for each in ad:
        send(each)
