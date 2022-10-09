from multiprocessing import context
import os
from email.message import EmailMessage
import ssl
import smtplib

#Step 1: Make Sure You Activate 2 Factor Auth On Your Google Account
#Step 2: Go To /apppaswords On Your Google Account Dashboard
#Step 3: Create A New App And Save Your Password Somewhere In Your Pc
#Step 4: Open The Text File From The Location You Saved It like Showen Bellow 
#Step 5: Setup Is Complete Follow Along And Enjoy
with open("C:\\Users\\jadna\\Desktop\\Youtube\\ps.txt","r") as ps1:
    ps = ps1.readlines()
    
#Initialze Your Variables     
email_sender = "jadnahle99@gmail.com"
email_password = ps[0]
email_reciver = "jadnadev@gmail.com"

#Set Your Email Content
subject = "Automated Email"
body = """
THIS IS AN AUTOMATED EMAIL
"""
#Instantiate Python Email Library 
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

#SSL Is A Security Protocol
context = ssl.create_default_context()

#Connecting To Gmail Servers 
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)as smtp :
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())

    