1. Create .bat file
   1a. Replace the appropriate paths to python executable (python.exe) on your PC and the path to the .py file within quotes.

2. Create .py file
   2a. Replace the "mail" portions with application from and from-password and enter email address to send the alert to.

3. use Windows Task Scheduler to set up the timing of when to use the .bat file which will call the .py file to run

4. The script should run at the designated times you set and send an email with the details of the current stock price and the percent of it's change from the previous trading day.

To do: Allow the email it sends from to take requests via email and send back results, such as Dividend yield, Quarterly Cashflow, Cash Reserves, etc.