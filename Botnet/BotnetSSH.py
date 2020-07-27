from selenium import webdriver
from time import sleep

browser=webdriver.Chrome(executable_path=r'C:\Users\olcay\PycharmProjects\botnet\drivers\chromedriver.exe')
browser.get('https://www.instagram.com/')

sleep(5)

browser.close()