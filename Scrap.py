import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# try:
driver = uc.Chrome()
driver.get("https://www.google.com")
time.sleep(random.uniform(3, 5))

search_box = driver.find_element(By.XPATH, '//textarea[@name="q"]')
search_box.send_keys("Campusx")
time.sleep(random.uniform(1, 2))
search_box.send_keys(Keys.ENTER)

time.sleep(5)

link = driver.find_element(by = By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()
time.sleep(3)

link2 = driver.find_element(by = By.XPATH,value='/html/body/div[1]/header/section[2]/a[1]')
link2.click()
time.sleep(1)
input("Press Enter to quit...")

# finally:
    # driver.quit()  # Ensures clean exit
