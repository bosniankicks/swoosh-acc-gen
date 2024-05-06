from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from random import randint
from time import sleep
import random
import os
import json


cookies_dir = 'co'
def mm(driver):
    x = randint(3,9)
    a = randint(1,9)
    s = randint(1,20)
    z = randint(100,900)
    n = randint(100,900)
    pointer = driver.current_pointer
    move_kwargs = {"total_time": 0.7, "accel": a, "smooth_soft": s}

    pointer.move_to(z, n)
    driver.sleep(1)
    pointer.click(n, z, move_kwargs=move_kwargs, move_to=True)
    driver.sleep(0.3)

def searchstuff(driver):
    driver.get('https://www.nike.com/')

    search_items = [
    "Air Max",
    "Jordan",
    "running shoes",
    "basketball shoes",
    "hoodies",
    "sports bras",
    "soccer cleats",
    "backpacks",
    "caps",
    "training pants",
    "Nike SB",
    "Yoga pants",
    "Dri-FIT tees",
    "golf polos",
    "skateboarding shoes",
    "tennis apparel",
    "kids' sneakers",
    "women's leggings",
    "men's shorts",
    "football gear",
    "Apple Watch Nike",
    "sunglasses",
    "socks",
    "jordan 1",
    "dunk",
    "slides",
    "jordans",
    "red sneakers",
    "air max 90",
    "Free Run",
    "Accessories",
    "blue"
    ]

    driver.sleep(2)
    searchinput = random.choice(search_items)
    search = driver.find_element(By.ID,'VisualSearchInput')
    js_script4 = """
    var inputField = document.getElementById('VisualSearchInput');
    inputField.value = '';  
    var event = new Event('input', { bubbles: true });
    inputField.dispatchEvent(event);
    """

    # Execute the script
    driver.execute_script(js_script4)
    driver.sleep(1)

    search.write(searchinput)
    driver.sleep(2)
    searchbtn = driver.find_element(By.CLASS_NAME,'pre-search-btn ripple')
    searchbtn.click()


# Function to process each account with its cookies
def process_account_with_cookies(cookie_file_path):

    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options=options) as driver:
        driver.set_window_size(400, 400)

      
        with open(cookie_file_path, 'r') as file:
            cookies = json.load(file)
            driver.get('https://www.nike.com/')
            for cookie in cookies:
                driver.add_cookie(cookie)

        driver.get('https://www.nike.com/inbox')
        sleep(3) 
        driver.set_window_state('maximized')
        sleep(4)
        driver.set_window_state('normal')
        sleep(3)
        driver.set_window_size(200, 400)
        sleep(5)

        driver.refresh() 
        driver.sleep(6)
        driver.refresh() 
        driver.get('https://www.nike.com/inbox')
        driver.sleep(3)

        contin = driver.find_element(By.CLASS_NAME,'nds-btn css-hj7pkf btn-primary-dark  btn-md')
        contin.click()

        driver.sleep(4)

        try:
            closer = driver.find_element(By.CLASS_NAME,'modal-close-btn css-1at3lj9 e1jdve9b0')
            closer.click()
            driver.sleep(5)
        except:
            driver.sleep(3)

        driver.get('https://www.nike.com/launch')
        driver.sleep(3)
        scroll_down_script = "window.scrollBy(0, 500);"
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        scroll_up_script = "window.scrollBy(0, -300);"
        driver.execute_script(scroll_up_script)

        try:
            closer = driver.find_element(By.CLASS_NAME,'modal-close-btn css-1at3lj9 e1jdve9b0')
            closer.click()
            driver.sleep(5)
        except:
            driver.sleep(5)

        searchstuff(driver)
        driver.sleep(6)
        searchstuff(driver)
        driver.sleep(4)
        searchstuff(driver)
        mm(driver)
        driver.sleep(10)

        mm(driver)
        mm(driver)
        mm(driver)
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        driver.execute_script(scroll_up_script)
        searchstuff(driver)
        print('new search')
        mm(driver)
        mm(driver)
        mm(driver)
        mm(driver)
        mm(driver)
        searchstuff(driver)
        print('2nd search')
        mm(driver)
        mm(driver)
        mm(driver)
        mm(driver)
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        driver.execute_script(scroll_up_script)
        mm(driver)
        mm(driver)
        searchstuff(driver)
        print('3rd search')
        mm(driver)
        mm(driver)
        mm(driver)
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        driver.execute_script(scroll_up_script)  
        mm(driver)
        searchstuff(driver)
        print('last search')
        mm(driver)
        mm(driver)
        mm(driver)
        mm(driver)
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        driver.execute_script(scroll_up_script)  
        mm(driver)
        driver.get('https://www.nike.com/')
        mm(driver)
        mm(driver)
        for c in range(10):
            mm(driver)
        driver.get('https://www.nike.com/')
        driver.execute_script(scroll_down_script)
        driver.sleep(2)
        driver.execute_script(scroll_up_script)
        for c in range(10):
            mm(driver)
        driver.quit()
        driver.close()
        print('Process has been finished')


if __name__ == '__main__':
    cookie_files = [f for f in os.listdir(cookies_dir) if f.endswith('.json')]
    for cookie_file in cookie_files:
        cookie_file_path = os.path.join(cookies_dir, cookie_file)
        process_account_with_cookies(cookie_file_path)
