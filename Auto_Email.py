from multiprocessing import context
import os
from email.message import EmailMessage
import ssl
import smtplib

with open("C:\\Users\\jadna\\Desktop\\Youtube\\ps.txt","r") as ps1:
    ps = ps1.readlines()
    
email_sender = "jadnahle99@gmail.com"
email_password = ps[0]
email_reciver = "jadnadev@gmail.com"

subject = "Automated Email"
body = """
THIS IS AN AUTOMATED EMAIL
"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_reciver
em["Subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context)as smtp :
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())

    