from selenium import webdriver
import os
import signal

# https://qiita.com/shobota/items/5324ca810b3848c4fd0f
try:
    browser = webdriver.Chrome()
    browser.get("https://scraping-for-beginner.herokuapp.com/login_page")
finally:
    os.kill(browser.service.process.pid, signal.SIGTERM)
