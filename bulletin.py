import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

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
		rows.pop(0)
		
		for row in rows:
			titles.append(row[2].split("\n")[0])
	sendEmail(titles)

#function to send e-mail
def sendEmail(titles):
	sender = "sender@gmail.com"
	recipient = "receiver@gmail.com"
	subject = "Haftalik Cizgi Romanlar"
	body = "Cizgi roman listesi: \n" + "\n".join(titles)

	msg = MIMEText(body)
	msg["Subject"] = subject
	msg["From"] = sender
	msg["To"] = recipient

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login('sender@gmail.com', 'password')
	server.send_message(msg)
	print("Mail gönderildi!")

scrape()
