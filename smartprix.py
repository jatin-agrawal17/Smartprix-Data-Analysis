import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = uc.Chrome()
driver.get('https://www.smartprix.com/mobiles')

wait = WebDriverWait(driver, 20)

#Click "Exclude Out Of Stock"
checkbox1 = wait.until(EC.presence_of_element_located((By.XPATH, '//label[contains(., "Exclude Out Of Stock")]/input')))
driver.execute_script("arguments[0].click();", checkbox1)
print("✅ First checkbox clicked.")

#Click "Exclude Upcoming"
exclude_upcoming = wait.until(EC.presence_of_element_located((By.XPATH, '//label[contains(., "Exclude Upcoming")]/input')))
driver.execute_script("arguments[0].click();", exclude_upcoming)
print("✅ 'Exclude Upcoming' clicked.")

# Scroll and auto-click Load More
old_height = driver.execute_script("return document.body.scrollHeight")
counter = 1

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    # Click "Load More" if visible
    try:
        load_more_btn = driver.find_element(By.XPATH, '//*[@id="app"]/main/div[1]/div[2]/div[3]')
        if load_more_btn.is_displayed():
            driver.execute_script("arguments[0].click();", load_more_btn)
            print("🟩 Clicked 'Load More' button.")
            time.sleep(3)
    except:
        print("ℹ️ No 'Load More' button this round.")

    new_height = driver.execute_script("return document.body.scrollHeight")
    print(f"Scroll #{counter} | Old Height: {old_height} | New Height: {new_height}")
    counter += 1

    if new_height == old_height:
        print("End reached.")
        break
    old_height = new_height


html = driver.page_source

with open('smartprix.html' , 'w', encoding='utf-8') as f:
    f.write(html)

input("Press Enter to exit...")
driver.quit()
