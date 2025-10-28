from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import os


options = webdriver.ChromeOptions()

options.add_argument("--incognito")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.maximize_window()


DOWNLOAD_DIR = "downloads/puc"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

try:
    print("Opening PUC search page...")
    driver.get("https://www.puc.pa.gov/search/document-search/?DocketNumber=&ReferenceDocketNumber=&eFilingConfirmationNumber=&CaseType=&PublicMeetingFromDate=&PublicMeetingToDate=&DocumentReceivedFromDate=&DocumentReceivedToDate=&DocumentServedFromDate=&DocumentServedToDate=&DocumentTitle=&DocumentType=&UtilityCode=&UtilityName=&UtilityType=2842707&ufprt=B31C3664AEDA3EA43C1B73036FA1AB93A779E733DB4A1C285376674325CF19A50C06B7A3B6F90212FC49D5C19E3CA57BC07B7A7FF7F49A806D9655CC0D07A66B5235CD168887D335BB72DBE67AA88249FBD7A91EFA0B1E82DB281E5A55B89DA9FD72EA4FD6032F9059794FE43D27575BA378E2EAE2D223C3B549961AF9B9435F14E4FA38FB8D7A00B3F1186DFFC77355F676B7536D2524A16BDE2B91FFA7F8C8CAFCDF19C0F69B6FC40B32A9526E624F858653BB80CE762DF10DE6734FD3CF60#search-results")
    time.sleep(5)

    
    print("Navigating to page 5...")
    driver.find_element(By.XPATH, "//a[normalize-space()='5']").click()
    time.sleep(3)

    
    print("Opening document page 1")
    doc_link = driver.find_element(By.LINK_TEXT, "NOTICE OF ENTRY OF APPEARANCE - APPLEBY ET AL/OCA")
    doc_link.click()
    time.sleep(3)

   
    pdf_url = driver.current_url
    #print(pdf_url)
    print(f"📄 Current URL: {pdf_url}")

    if pdf_url.lower().endswith(".pdf"):
        print("✅ PDF link detected. Downloading...")

        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(pdf_url))
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()

        with open(filename, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)

        print(f"✅ Download complete: {filename}")
    else:
        print("❌ PDF URL not detected. Maybe the redirect didn't complete?")

    
    print("Returning to main document search page...")
    driver.back()
    time.sleep(3)
    
    
    print("Opening document page 2")
    doc_link = driver.find_element(By.LINK_TEXT, "CERTIFICATE OF SATISFACTION - FE PA")
    doc_link.click()
    time.sleep(3)

   
    pdf_url = driver.current_url
    #print(pdf_url)
    print(f"📄 Current URL: {pdf_url}")

    if pdf_url.lower().endswith(".pdf"):
        print("✅ PDF link detected. Downloading...")

        filename = os.path.join(DOWNLOAD_DIR, os.path.basename(pdf_url))
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()

        with open(filename, "wb") as f:
            for chunk in response.iter_content(8192):
                f.write(chunk)

        print(f"✅ Download complete: {filename}")
    else:
        print("❌ PDF URL not detected. Maybe the redirect didn't complete?")
    
finally:
    driver.quit()
    print("Closed browser.")
