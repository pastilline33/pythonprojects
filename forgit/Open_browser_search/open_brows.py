
## This script uses the webbrowser library to use basic browser functions,
##  such as opening a browser tab and performing a search query on Google, 
## Yahoo Finance, or Amazon.

import webbrowser

# Opens a new browser window, typically Internet Explorer (even if your default browser is Chrome, Firefox, etc.)
# def search_web():
#     webbrowser.open("google.com")
#     return
    
# Prompts user for a google search query and opens a new tab in your default browser using 'windows-default'
# def search_web2():
#     query = input("What would you like me to search for?\n")
#     print("Returning results for " + query + " ..")
#     webbrowser.get('windows-default').open('http://www.google.com/search?q=' + query)
#     return


# Prompts user for Stock Symbol and performs a Yahoo Finance search in a new tab on your default browser
# def ticker_search():
#     query = input("What stock symbol you like me to search for?\n")
#     print("Returning results for " + query + " from Yahoo Finance..")
#     webbrowser.get('windows-default').open('https://finance.yahoo.com/quote/' + query)
#     return

# Prompts user for Amazon search query and performs search on Amazon
def amazon_search():
    
    while 1:
        amazon_query = input("Search on Amazon (Hit CTRL-Z to cancel): ")
        print("Returning results for " + amazon_query + " from Amazon...")
        webbrowser.get('windows-default').open('https://www.amazon.com/s?k=' + amazon_query)
        amazon_search()
        return
    

## Opens a browser tab in default browser 
## webbrowser.get('windows-default').open('http://www.google.com') 

## New tab with a search template (/search?q=XXX)
## webbrowser.get('windows-default').open('http://www.google.com/search?q=dogs

# search_web()
# search_web2()
# ticker_search()
amazon_search()