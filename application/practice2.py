from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import signal

# https://qiita.com/shobota/items/5324ca810b3848c4fd0f
try:
    browser = webdriver.Chrome()
    browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")
finally:
    os.kill(browser.service.process.pid, signal.SIGTERM)
