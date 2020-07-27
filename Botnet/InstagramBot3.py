from time import sleep
from selenium import webdriver
from crediantials import username,password,ss,username3,password3,username2,password2
from time import sleep

browser = webdriver.Chrome(executable_path=r'C:\Users\olcay\PycharmProjects\botnet\drivers\chromedriver.exe')
browser.implicitly_wait(5)
browser.get('https://www.instagram.com/')

def bum(user,paswd):

    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(user)
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(paswd)
    browser.find_element_by_css_selector('button[type=submit').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input').send_keys(ss)
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/main/div/header/section/div[1]/div[3]/button').click()
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div/button[3]').click()
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div/div/div/div[2]/button').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span').click()
    browser.find_element_by_xpath(
        '/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div').click()
    sleep(5)

bum(username3,password3)
browser.close()

"""
browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()
browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[2]').click()
browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[1]').click()
browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[2]/div/div/div/div[3]/button[5]').click()
browser.find_element_by_xpath(
    '/html/body/div[4]/div/div/div/div[2]/div/div/button').click()
"""