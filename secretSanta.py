import random
import smtplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

names = []
emails = []
order = []

message = "Thank you for participating in Songbird Secret Santa 2018!\n Here is some information to know:\n\n1. Gifts will be exchanged at the Songbird Holiday Party December 9th. \n2. Gifts should be $20 or less. \n3. KEEP IT A SECRET!\n\nYou are the secret santa of: "
subject = "ACTUAL Songbird Secret Santa 2018"
spreadsheet = "https://docs.google.com/spreadsheets/d/1ohOJa27hxMCQNGuUgC12YZrFMdXBQF5DLDo2BBjGyd4/edit?usp=sharing"
ender = "Please see the link below and add your interests to the spreadsheet so your secret santa can get some ideas for a gift for you! \n" + spreadsheet + "\n\n Happy Holidays!"

file = open("/Users/eliturner/Documents/Python Projects/Secret Santa/juice.txt",'r')
for line in file:
    splitline = line.split()
    names.append(splitline[0])
    emails.append(splitline[1])

for i in range(len(names)):
    order.append(i)

random.shuffle(order)

myemail = "songbirdSS2018@gmail.com"
mypsswrd = "constjuice"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(myemail, mypsswrd)

for i in range(len(names)):
    greeting = "Dear " + names[order[i]] + ",\n\n"
    msg = MIMEMultipart()
    msg["From"] = myemail
    msg["To"] = emails[order[i]]
    msg["Subject"] = "Secret Santa 2018"
    msg.attach(MIMEText(greeting + message + names[order[(i+1)%(len(names))]] + "\n\n" + ender, "plain"))
    text = msg.as_string()
    server.sendmail(myemail, emails[order[i]], text)
