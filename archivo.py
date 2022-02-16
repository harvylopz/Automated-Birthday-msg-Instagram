from email import message
from http.client import BAD_GATEWAY
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time
import random
import pandas as pd
from datetime import datetime

# driver = webdriver.Chrome(r"C:\Users\harvylaptop\dev\Automated-Birthday-msg-Instagram\chromedriver")

#Usuario y contraseña de la persona que va a enviar los mensajes


def path():
    global chrome
    chrome = webdriver.Chrome()

def url_name(url):
    chrome.get(url)
    time.sleep(4) #time seconds

def login(username, password):
    #accept cookies
    # cookies = chrome.find_element_by_class_name("bIiDR")
    # cookies.click()
    # time.sleep(3)

    log_but = chrome.find_element_by_class_name("L3NKy")
    log_but.click()
    time.sleep(3)

    usern = chrome.find_element_by_name("username")
    usern.send_keys(username)

    passw = chrome.find_element_by_name("password")
    passw.send_keys(password)

    passw.send_keys(Keys.RETURN)
    time.sleep(5)

    notk = chrome.find_element_by_class_name("yWX7d")
    notk.click()
    time.sleep(4)

def send_message():
    message=chrome.find_element_by_class_name("_8A5w5")
    message.click()
    time.sleep(4)

    not_now=chrome.find_element_by_class_name("HoLwm")
    not_now.click()
    time.sleep(3)

    mbox=chrome.find_element_by_tag_name("textarea")
    mbox.send_keys("Happy Birthday")
    mbox.send_keys(Keys.RETURN)
    time.sleep(3)

def birthdaycheck():
    
    bday=pd.read_excel("birthday-data.xlsx")
    bday["month"]=pd.DatetimeIndex(bday["birthdate"]).month
    bday["day"]=pd.DatetimeIndex(bday["birthdate"]).day
    
    name=list(bday["name"])

    birthdate_month=list(bday["month"])

    birthdate_day=list(bday["day"])

    instaname=list(bday["instaname"])

    dictionary={}
    for i in range(len(name)):
        dictionary[name[i]]=(birthdate_month[i],birthdate_day[i],instaname[i])

    date=datetime.now().month,datetime.now().day

    instanames = []
    for i in dictionary:
        if dictionary[i][0:2]==date:
            instanames.append(dictionary[i][-1])
    return (instanames)
    



path()
instanames=birthdaycheck()
time.sleep(1)
birthdaycheck()

for i in instanames:
    url="https://instagram.com/" + i
    url_name(url)
    login("YourUserName", "Yourpassword")
    send_message()
    chrome.close()



