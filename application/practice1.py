from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import signal

# https://qiita.com/shobota/items/5324ca810b3848c4fd0f
try:
    browser = webdriver.Chrome()
    browser.get("https://scraping-for-beginner.herokuapp.com/login_page")
    # 要素を指定
    username = browser.find_element(By.ID, value="username")
    password = browser.find_element(By.ID, value="password")
    login_btn = browser.find_element(By.ID, value="login-btn")
    username.send_keys("imanishi")
    password.send_keys("kohei")
    login_btn.click()
    name = browser.find_element(By.ID, value="name")
    company = browser.find_element(By.ID, value="company")
    birthday = browser.find_element(By.ID, value="birthday")
    come_from = browser.find_element(By.ID, value="come_from")
    hobby = browser.find_element(By.ID, value="hobby")
    # 複数のelementをlistとしてまとめて取得
    th_elements = browser.find_elements(By.TAG_NAME, value="th")
    td_elements = browser.find_elements(By.TAG_NAME, value="td")
    for i in range(len(th_elements)):
        print(th_elements[i].text)
    for i in range(len(td_elements)):
        print(td_elements[i].text)
finally:
    os.kill(browser.service.process.pid, signal.SIGTERM)
