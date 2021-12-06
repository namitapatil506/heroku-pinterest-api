# with parameter passed

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re
# import pandas as pd
import time
import requests
from flask import Flask, render_template, request, redirect, url_for
from urllib3.util import url
from werkzeug.utils import secure_filename

APP_ROOT=os.path.dirname(os.path.abspath(__file__))

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'UPLOAD_FOLDER/'
@app.route('/pin_api',methods=['POST'])
def pin_automate():
    username=request.args.get('username')
    password=request.args.get('password')
    file=request.files.get('file')
    filename = secure_filename(file.name) + '_video' + '.mp4'
    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    driver = webdriver.Chrome(executable_path='E:/namita/chromedriver_win32/chromedriver')  # path of chromedriver
    driver.get('https://in.pinterest.com/idea-pin-builder/')
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[1]/div[2]/div[2]/button').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[1]/fieldset/span/div/input').send_keys(username)  # input in api
    driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[2]/fieldset/span/div/input').send_keys(password)  # input in api
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div/div/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button').click()
    time.sleep(25)
    driver.find_element_by_xpath('//*[@id="HeaderContent"]/div/div/div/div/div[2]/div/div/div/div[2]/div/button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="HeaderContent"]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a/div/div').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div[1]/div[2]/div/div/div/div[1]/div/div[3]/div/button').click()
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="storyboard-upload-input"]').send_keys(f'E:/namita/TG/pinterest_api/UPLOAD_FOLDER/{filename}')  # input in api
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[3]/div[3]/div/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="storyboard-selector-title"]').send_keys('testing')  # input in api
    driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[4]/div[3]/div/div/div[2]/button').click()

    return render_template('successful.html')


if __name__ =="__main__":
    app.run(debug=True)