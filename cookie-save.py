from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from selenium.webdriver.common.keys import Keys
import json
import os

if not os.path.exists('co'):
    os.makedirs('co')


with open('accs2.txt', 'r') as emails_file:
    accounts = [line.strip() for line in emails_file.readlines()]


def handle_account(email, pasw):
    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options=options) as driver:
        driver.get('https://nike.com/register')
        driver.sleep(5)
        emailinp = driver.find_element(By.ID,'username')
        emailinp.write(email)
        emailcontinuebutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/form/div/div[4]/button')
        emailcontinuebutton.click()
        driver.sleep(3)
        passlogin = driver.find_element(By.ID,'password')
        passlogin.write(pasw)
        driver.sleep(6)
        pasbtn = driver.find_element(By.CLASS_NAME,'nds-btn css-hj7pkf btn-primary-dark  btn-md')
        pasbtn.click()
        driver.sleep(15)
        input('click enter when ready') #just used this to manually enter codes in
        driver.get('https://www.nike.com/orders')
        driver.sleep(5)

        inbox = driver.find_element(By.CLASS_NAME,'u-full-width d-sm-b ta-sm-l typography-body-1-strong pr4-sm pl4-lg')
        inbox.click()

        driver.sleep(8)

        cookies = driver.get_cookies()
        cookie_filename = f'co/cookies-{pasw}.json'
        with open(cookie_filename, 'w') as f:
            json.dump(cookies, f)
        driver.sleep(15)
        driver.quit()
        driver.close()

for account in accounts:
    if ':' in account:
        email, pasw = account.split(':', 1)
        handle_account(email, pasw)
    else:
        print(f"Skipping line due to incorrect format: {account}")

    


    


