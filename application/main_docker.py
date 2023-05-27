# from selenium import webdriver
# import os
# import signal

# # https://qiita.com/shobota/items/5324ca810b3848c4fd0f
# try:
#     browser = webdriver.Chrome()
#     browser.get("https://scraping-for-beginner.herokuapp.com/login_page")
# finally:
#     os.kill(browser.service.process.pid, signal.SIGTERM)
from selenium import webdriver

browser = webdriver.Remote(
    "http://selenium-hub:4444/wd/hub",
    desired_capabilities={"browserName": "chrome"},
)

# ログインページにアクセスします
browser.get("https://scraping-for-beginner.herokuapp.com/login_page")

# ブラウザを終了します
browser.quit()
