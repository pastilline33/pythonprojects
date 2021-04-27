Requirements:
1. BestBuy Account
2. Fill out Best Buy account details on the website (Credit card, shipping address and preferred store). Only checks one store at a time currently (the one you have set as preferred).
3. Fill out details within the script: BestBuy account username/password, Credit card three digit security code.
4. For email notification, fill out your email providers SMTP address and port, sender email address / password and receiving email address. In stock alerts will be sent to your email address with emojis to help the email stand out.

This python script will work with Google Chrome version 90 browsers (most current at this time). The script will check the page listed in the URL every 8 seconds, including a timestamp and email notification.

It works well for one item at a time but multiple copies of the script, with different items, will work best. The python executable will provide the item description, in/out of stock status and timestamp. If the page reloads and detects an in stock item it will immediately begin the checkout process from start to finish. I am working to add an additional print line that puts out the Order Confirmation number, but for now it will be sent to your email through the normal checkout process.

Once the script successfully purchases an item the script will need to be restarted manually.


