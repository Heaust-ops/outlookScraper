from selenium import webdriver
from time import  sleep
from config import *
from os import path
script_path = path.dirname(path.abspath( __file__ ))

class outlookBot():
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=script_path+r'/geckodriver')
    
    def login(self):
        self.driver.get('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1584179991&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3dab9b6d22-4a43-52a9-57c7-f37ccfd96ebd&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')
        next_btn = self.driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        email_in = self.driver.find_element_by_xpath('//*[@id="i0116"]')
        pass_in = self.driver.find_element_by_xpath('//*[@id="i0118"]')
        email_in.send_keys(email)
        sleep(2)
        next_btn.click()
        pass_in.send_keys(password)
        sleep(2)
        sign_btn = self.driver.find_element_by_xpath('//*[@id="idSIButton9"]')
        sign_btn.click()

bot = outlookBot()
bot.login()