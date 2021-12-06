# without parameter passed


import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
# import pandas as pd
import time
import requests
from flask import Flask, render_template, request, redirect, url_for

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__)

@app.route('/')
def pin_automate():
    driver = webdriver.Chrome(executable_path='E:/namita/chromedriver_win32/chromedriver')  # path of chromedriver
    driver.get('https://in.pinterest.com/idea-pin-builder/')
    driver.find_element_by_xpath(
        '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button').click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[1]/fieldset/span/div/input').send_keys(
        'tg.tech02@gmail.com')  # input in api
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[2]/fieldset/span/div/input').send_keys(
        'Nitesh@12')  # input in api
    driver.find_element_by_xpath(
        '//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button').click()
    time.sleep(20)
    driver.find_element_by_xpath(
        '//*[@id="HeaderContent"]/div/div/div/div/div[2]/div/div/div/div[2]/div/button').click()
    time.sleep(10)
    driver.find_element_by_xpath(
        '//*[@id="HeaderContent"]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a/div/div').click()
    time.sleep(10)
    driver.find_element_by_xpath(
        '//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="storyboard-upload-input"]').send_keys(
        'E:/namita/TIKTOK.mp4')  # input in api
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div[3]/div/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="storyboard-selector-title"]').send_keys('testing')  # input in api
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div[3]/div/div/div[2]/button').click()

    return 'successful'


if __name__ =="__main__":
    app.run(debug=True, use_reloader=False)