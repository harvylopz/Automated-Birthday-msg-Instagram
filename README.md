# Automated Birthday Message on Instagram

This script automates the sending of birthday messages on Instagram to users whose birthdays are in the "birthday-data.xlsx" file. This code uses the Python "Selenium" module to control the web browser and send the messages.

## Requirements

- Have Python 3 installed
- Install required modules: email, http.client, webbrowser, selenium, pandas, and datetime.
- Download the Google Chrome driver and specify the path in the code.
- Provide Instagram username and password.
- Have an Excel file with names, birthdates, and Instagram username of message recipients.

## How it works

1. The script imports the necessary modules and reads the "birthday-data.xlsx" file with the help of pandas.
2. The datetime module is used to get the current month and day.
3. The birthday months and days are compared to the current date and a list of Instagram usernames of those who have birthdays is created.
4. The Chrome browser is initialized with Selenium.
5. The list of Instagram usernames is traversed and their profile is accessed.
6. The provided Instagram account is logged in and the birthday message is sent.
7. The browser is closed and the process is repeated for the next user.

## Notes

- It is possible that Instagram may block the account for the use of an automated script. It is recommended to use this tool with caution and responsibility.
- Make sure not to infringe on Instagram's privacy policies and terms of service.
- This code is for educational purposes only and the author is not responsible for any damage or loss that may arise from the use of this script.
