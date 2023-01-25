import time
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  #WEBブラウザの起動

# 定数
TARGET_URL = "https://laquan.com/login.jsp"
USERNAME = "<YOUR_USERNAME>"
PASSWORD = "<YOUR_PASSWORD>"
PHOTO_NUM = 90 # ダウンロード対象の写真の数

# トップページへアクセス
driver.get(TARGET_URL)

time.sleep(1)

# ログイン処理
mail = driver.find_element(By.ID, "signinEmail")
password=driver.find_element(By.ID, "signinPassword")
browser_from = driver.find_element(By.ID, "signin_submit")

mail.clear()
password.clear()

mail.send_keys(USERNAME)
password.send_keys(PASSWORD)

browser_from.click()
time.sleep(1)

# ダウンロードリンクボタンクリック
dlLink = driver.find_element(By.XPATH, "//ul[@class='photosetoperation']/li[3]")
dlLink.click()

# 画像をダウンロード
for n in range(PHOTO_NUM):
  correct_xpath = "//ul[@class='photoThumList']/div[" + str(n+1) + "]/a";
  pic = driver.find_element(By.XPATH, correct_xpath)
  pic.click()
  time.sleep(3)
