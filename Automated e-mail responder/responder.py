import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import schedule
import time

#for email Configs such as sender and reciever settings.
SMTP_SERVER = 'smrtp.gmail.com' #example  gmail or anothe email
SMTP_PORT = 587 #FOR SSL USE 465
SMTP_USERNAME = 'your _email@gmail.com' #your email.
SMTP_PASSWORD = 'ypur_password'
FROM_EMAIL = 'your_email@gmail.com'#gmail or @example.com for senders email address.
TO_EMAIL = 'reciepient_email@eample.com' #recievers email address.


#define a function to generate the email content.
def create_email(subject, body):
    msg = MIMEMultipart()
    msg['from'] = FROM_EMAIL
    msg['TO'] = TO_EMAIL
    msg['subject'] = subject

    msg.attach(MIMEText(body, 'plain'))
    return msg

#define a function to send email.
def send_email(msg):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print('Email sent succesfully.')
    except Exception as e:
        print(f'Failed to send email: {e}')

#define the main function to combine the above functions and create, send e-mails. 
def send_daily_report():
    subject = "Daily Report"
    body = "Hello mr/mrs. ****, This is the Daily E-mail report content." 

    email = create_email(subject, body)
    send_email(email)

#using the "schedule" library to run 'send_daily_report' function at a specific time regularly. 
def job():
    send_daily_report()

    #schedule your time:
    schedule.every().day.at("08.00").do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

        


