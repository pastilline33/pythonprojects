### This script + Windows Task Scheduler will allow the script to run at predetermined times
### and send an email alert about the price of the stock selected. It only works
### for one stock at a time.
### todo: implement requests received from email to lookup stocks and send back data.

import yfinance
import smtplib
from email.mime.text import MIMEText

print("Running stock price check")
selected_stock = "BABA"
stock = yfinance.Ticker(selected_stock)

aval = stock.info["regularMarketPrice"]
bval = stock.info["previousClose"]
cval = ((aval - bval)/bval)*100

daychange = (str(round(cval, 2)))

# print(daychange)

if (float(daychange)) <= 0:
    up_or_down = " down "
else:
    up_or_down = " up "

# print(up_or_down)




SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "email"
SMTP_PASSWORD = "password"
EMAIL_FROM = "email"
EMAIL_TO = "email"
EMAIL_SUBJECT = "REMINDER:" 
co_msg = """Hello, [username]! Just wanted to send a friendly notice that """+ selected_stock +" stock is currently trading at " + (str(aval)) + " USD,"+ (str(up_or_down)) + (str(daychange)) + """% for the day. This script will run every 5 minutes 
  for one day. The Email Subject was: """ + EMAIL_SUBJECT




# try:
#     print("Current price (USD) of " + stock.info["shortName"] + " (Symbol:" + stock.info["symbol"] + ") " + "is: ")
#     print(stock.info["regularMarketPrice"])
# except:
#     print("Stonk not found.")
#     quit()

def send_email():
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT + "Stock Price Alert"
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()

# if stock.info["regularMarketPrice"] <= 200:
send_email()
print(selected_stock + " stock is currently trading at " + (str(aval)) + " USD,"+ (str(up_or_down)) + (str(daychange)) + "% for the day." )
print("Email sent to " + EMAIL_TO + ". ")

