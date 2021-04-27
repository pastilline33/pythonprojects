from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import smtplib
from email.mime.text import MIMEText
import time

cart_url = 'https://bestbuy.com/cart'
gpu_url = 'https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440'

selectedGPU = "NVIDIA GeForce RTX 3080 10GB GDDR6X"

def send_email():
    datime = time.strftime('%H:%M:%S')
    msg = MIMEText(co_msg)
    msg['Subject'] = EMAIL_SUBJECT
    msg['From'] = EMAIL_FROM 
    msg['To'] = EMAIL_TO
    debuglevel = True
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    print("Email sent to " + EMAIL_TO + " at " + datime + ". ")
    mail.quit()

# BestBuy Login Creds/Credit Card Security Code
userCred="email"
passCred="password"
cardCode="000"

# Opens Chrome browser
browser = webdriver.Chrome()

# Directs browser to url
browser.get(gpu_url)

# Locates and Clicks BestBuy yellow add to cart button on item page
addToCartButton = browser.find_element_by_class_name('add-to-cart-button')

def main():

    while 1:
        # Timestamps
        datime = time.strftime('%H:%M:%S')
        
        addToCartButton = browser.find_element_by_class_name('add-to-cart-button')
        time.sleep(1)
        if addToCartButton.text == 'Add to Cart':
            print('ALERT: ITEM ' + selectedGPU + ' AVAILABLE!!!' + datime)

            addToCartButton.click()
            browser.get(cart_url)
            time.sleep(3)
            test_Checkoutbtn = browser.find_element_by_class_name('btn-primary')
            test_Checkoutbtn.click()

            print("ALERT:Yellow checkout button clicked!!!" + datime)

            # Enter Username
            time.sleep(5)
            enterUsername = browser.find_element_by_id('fld-e')
            enterUsername.send_keys(userCred)

            # Enter Password
            enterPassword = browser.find_element_by_id('fld-p1')
            enterPassword.send_keys(passCred)

            # Click Sign In button
            signInButton = browser.find_element_by_class_name('cia-form__controls__submit')
            signInButton.click()

            # (Place Your Order Page) Enter Credit Card Security Code
            time.sleep(5)
            securityCodeButton = browser.find_element_by_class_name('form-control')
            securityCodeButton.send_keys(cardCode)

            # Place Your Order
            placeYourOrder = browser.find_element_by_class_name('button__fast-track')
            placeYourOrder.click()

            send_email()
            quit

        elif addToCartButton.text == 'Sold Out':
            print('*Item ' + selectedGPU  +' out of stock...' + datime)
            time.sleep(3)
            browser.refresh()
            time.sleep(5)
        else:
            print("Exception occured, unknown reason" + datime)
            time.sleep(3)
            browser.refresh()
            time.sleep(5)

# Email notification
SMTP_SERVER = "some mail server"
SMTP_PORT = 587
SMTP_USERNAME = "email"
SMTP_PASSWORD = "email password"
EMAIL_FROM = "email"
EMAIL_TO = "receiver email"
EMAIL_SUBJECT = "✨🏄‍♂️⭐ ALERT: " + selectedGPU + " 🤚 in stock!!"
co_msg = "Hello, [username]! Just wanted to send a friendly notice that " + selectedGPU + "  is currently in stock at " + gpu_url

main()

