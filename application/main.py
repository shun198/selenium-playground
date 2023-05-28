from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import (
    presence_of_element_located,
)
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    command_executor="http://selenium-hub:4444/wd/hub",
    desired_capabilities=DesiredCapabilities.CHROME.copy(),
)
# ドライバとタイムアウト値を指定
wait = WebDriverWait(driver, 10)
# ログインページにアクセスします
driver.get("https://google.com")
# "selenium"で検索
driver.find_element(By.NAME, "q").send_keys("selenium" + Keys.RETURN)
# 1件目の検索結果を取得(描画されるまで待機)
first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3")))
print(first_result.get_attribute("textContent"))

driver.quit()
