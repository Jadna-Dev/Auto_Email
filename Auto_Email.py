from multiprocessing import context
from email.message import EmailMessage
import ssl
import smtplib

#Text File Containing Your Google Account App Password
with open("C:\\Users\\jadna\\Desktop\\Youtube\\ps.txt") as ps1:
    ps = ps1.read()
    
#Initialize Your Variables
email_sender = "jadnahle99@gmail.com"
email_password = ps
email_reciver = ""

#set Your Email Content
subject = "Automated Email"
body = """
THIS IS AN AUTOMATED EMAIL
"""
#Instantiate Python Email Library
em = EmailMessage()
em["From"] = email_reciver
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

#SSL Is A Security Protocol
context = ssl.create_default_context()

#Connecting To Gmail Servers And Sending The Mail
#Open List Containing The Emails
with open("./EmailLists.txt", "r") as emaillst1:
    emaillst = emaillst1.readlines()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp :
    smtp.login(email_sender, email_password)
    for i in emaillst:
        email_reciver = i
        smtp.sendmail(email_sender, email_reciver, em.as_string())