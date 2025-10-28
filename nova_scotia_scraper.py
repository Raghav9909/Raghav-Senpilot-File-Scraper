from selenium import webdriver
from selenium.webdriver.common.by import By
import time


options = webdriver.ChromeOptions()

driver = webdriver.Chrome(options=options)
driver.maximize_window()

try:
    print("Opening site...")
    driver.get("https://uarb.novascotia.ca/fmi/webd/UARB15")
    time.sleep(10)  # give WebDirect time to load fully

    
    print("Navigating...")
    driver.find_element(By.CSS_SELECTOR, "#b0p0o193i0i0r1 div.icon-wrapper > div").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#b0p0o216i0i0r1 > div").click()
    time.sleep(10)
    driver.find_element(By.XPATH, "//span[contains(text(),'E-ANT-C-08:  Complaint by St. F.X. et al. against ')]").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "div.fm_object_277 span span").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#b0p1o308i1i0r1 span span").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "div.v-slot-primary > div > span").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "div.v-slot-fm-download-form div > span").click()
    time.sleep(10)


    print("✅ Completed basic navigation and download sequence.")

finally:
    driver.quit()
    print("Closed browser.")
