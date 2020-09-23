import requests
from bs4 import BeautifulSoup
import time
import smtplib
runs = 0
while True:
    url = "" #url of website to monitor
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get (url, headers=headers)
    soup = BeautifulSoup(response.text,"lxml")
    if str(soup).find("Available online") == -1: #look for look for specific text
            time.sleep(60)
            continue
    else:
            #generate email and send
            msg = "Subject: Back in stock!" #subject line
            fromaddr = '555@gmail.com'
            toaddrs = ['555@gmail.com']

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login ('555@gmail.com', 'password') #email username and password

            print('From: ' + fromaddr)
            print('To: ' + str(toaddrs))
            print('Message: ' + msg)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit
            print ("finished")
            break
