import os
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

fullName = os.getenv("FULL_NAME")
phone = os.getenv("PHONE")
email = os.getenv("EMAIL")

LOG_FILE = "run_log.txt"

def runs_this_week():
    if not os.path.exists(LOG_FILE):
        return 0

    with open(LOG_FILE, "r") as f:
        timestamps = [line.strip() for line in f.readlines() if line.strip()]

    now = datetime.datetime.utcnow()
    days_since_sunday = now.weekday() + 1 if now.weekday() != 6 else 0
    sunday_start = (now - datetime.timedelta(days=days_since_sunday)).replace(
        hour=0, minute=0, second=0, microsecond=0
    )

    count = 0
    for t in timestamps:
        try:
            t_dt = datetime.datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
            if t_dt >= sunday_start:
                count += 1
        except ValueError:
            continue

    return count

def log_run():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    with open(LOG_FILE, "a") as f:
        f.write(now + "\n")

def run_bot():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://waitwhile.com/locations/basicneeds/welcome?registration=waitlist")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="wwpp-container-inner"]/div[2]/form/div[1]/div/div/div/div[2]/button'))
    )
    driver.find_element(By.XPATH, '//*[@id="wwpp-container-inner"]/div[2]/form/div[1]/div/div/div/div[2]/button').click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="form_name"]'))
    )
    driver.find_element(By.XPATH, '//*[@id="form_name"]').send_keys(fullName)
    driver.find_element(By.XPATH, '//*[@id="form_phone"]').send_keys(phone)
    driver.find_element(By.XPATH, '//*[@id="form_email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="wwpp-container-inner"]/div[2]/form/div[2]/div/div/button').click()

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    count = runs_this_week()
    print(f"✅ Runs this week so far: {count}")

    if count >= 2:
        print("🚫 Limit reached — script will not run again this week.")
    else:
        run_bot()
        log_run()
        print("✅ Script completed and logged successfully.")
