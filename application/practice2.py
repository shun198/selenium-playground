from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import signal

# https://qiita.com/shobota/items/5324ca810b3848c4fd0f
try:
    browser = webdriver.Chrome()
    browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")
    rankingBox = browser.find_element(By.CLASS_NAME, "u_areaListRankingBox")
    title = (
        rankingBox.find_element(By.CLASS_NAME, "u_title")
        .find_element(By.TAG_NAME, "h2")
        .text.split("\n")[1]
        .split(" ")[0]
    )
    evaluate_number = (
        browser.find_element(By.CLASS_NAME, "u_rankBox")
        .find_element(By.CLASS_NAME, "evaluateNumber")
        .text
    )
    category = browser.find_element(By.CLASS_NAME, "u_categoryTipsItem")
finally:
    os.kill(browser.service.process.pid, signal.SIGTERM)
