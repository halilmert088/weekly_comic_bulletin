import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import json

#Function to scrape the weekly releases from comics.org
def scrape():
        titles = []
        headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        }

        for i in range(1, 2):
                url = "https://www.comics.org/on_sale_weekly/?page=" + str(i)
                response = requests.get(url, headers=headers)
                html_text = response.content

                soup = BeautifulSoup(html_text, 'html.parser')

                table = soup.find('table', {'class': 'sortable_listing'})

                rows = []
                for row in table.find_all('tr'):
                        cells = [cell.text.strip() for cell in row.find_all('td')]
                        rows.append(cells)
                rows.pop(0) #First element of the table in the website is empty so we pop it

                #Isolate the book title from the scraped data
                for row in rows:
                        titles.append(row[2].split("\n")[0])
        sendEmail(titles)

#function to send e-mail
def sendEmail(titles):
        with open('mailConfig.json') as config_file:
                data = json.load(config_file)

        sender = data['sender']
        recipient = data['recipient']
        subject = data['subject']
        body = "Cizgi roman listesi: \n" + "\n".join(titles)
        smtp_server = data['smtp_server']
        smtp_port = data['smtp_port']
        login_email = data['login_email']
        login_pass = data['login_pass']

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        #FOR TLS CONNECTION DELETE THE LINE ABOVE AND UNCOMMENT THE ONES BELOW
        #server = smtplib.SMTP(smtp_server, smtp_port)
        #server.starttls()
        server.login(login_email, login_pass)
        server.send_message(msg)
        print("Mail gönderildi!")

scrape()
