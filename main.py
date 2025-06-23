from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("chromedriver.exe"))
driver.get("https://bempenusa.cloud/login")
time.sleep(2)

try:
    # Uji SQL Injection
    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")

    username_input.send_keys("admin' OR '1'='1")
    password_input.send_keys("anything")
    login_button.click()

    time.sleep(3)

    if "dashboard" in driver.current_url:
        print("⚠️ POTENSIAL VULNERABILITAS: Login berhasil dengan SQL Injection.")
    else:
        print("✅ Aman: Login gagal dengan SQL Injection.")
except Exception as e:
    print("❌ Error saat pengujian:", e)

driver.quit()
