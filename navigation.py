from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--headless=new")

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://gyawunmusic.vercel.app")
    print("Opened Gyawun")


    section = driver.find_element(By.TAG_NAME, "section")
    link = section.find_element(By.TAG_NAME, "a")
    link.click()
    print("Clicked Download button")
    sleep(3)

    driver.back()
    print("Go Back")
    sleep(3)

    driver.forward()
    print("Go Forward")
    sleep(3)

    driver.refresh()
    print("Refresh page")
    sleep(3)
    

finally:
    # step 6: quit browser
    driver.quit()
    print("Test Completed")
