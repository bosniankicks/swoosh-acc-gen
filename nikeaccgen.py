from selenium_driverless.sync import webdriver
from selenium_driverless.types.by import By
from faker import Faker
from random import randint
import requests
import imaplib
import email
import imaplib
import time
import threading
api_key = ''
service = 'ew'
country = '16'
import re


def process_email(emaill):
    options = webdriver.ChromeOptions()
    with webdriver.Chrome(options=options) as driver:
    #driver.set_single_proxy(proxy)
    
        fake = Faker()
        fname = fake.first_name()
        lname = fake.last_name()
        passw1 = randint(1000,9999)
        passw = str(passw1)+fname+lname+"11!!"

        driver.get('https://nike.com/register')
        driver.sleep(5)
        emailinp = driver.find_element(By.ID,'username')

 
        emailinp.write(emaill)
        driver.sleep(1)
        emailcontinuebutton = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/form/div/div[4]/button')
        emailcontinuebutton.click()
        driver.sleep(3)

        passinp = driver.find_element(By.ID,'l7r-password-input')
        passinp.write(passw)
        driver.sleep(2)

        fnameinp = driver.find_element(By.ID,'l7r-first-name-input')
        fnameinp.write(fname)
        driver.sleep(1.5)


        lnameinp = driver.find_element(By.ID,'l7r-last-name-input')
        lnameinp.write(lname)
        driver.sleep(3)
        print('hello!!!!!!!')

        js_code = """
    var selectElement = document.querySelector('select');
    selectElement.innerHTML += '<option value="MENS">Men\\'s</option>';
    selectElement.value = 'MENS';
    var event = new Event('change', { 'bubbles': true, 'cancelable': true });
    selectElement.dispatchEvent(event);
    """

        driver.execute_script(js_code)
        driver.sleep(5)

        minp = driver.find_element(By.ID,'month')
        minp.write('4')
        driver.sleep(1)

        dinp = driver.find_element(By.ID,'day')
        dinp.write('14')
        driver.sleep(1)

        yinp = driver.find_element(By.ID,'year')
        yinp.write('2000')
  
        driver.sleep(10)


# Your Gmail credentials and server
        email_user = ''
        email_password = ''  
        imap_url = 'imap.gmail.com'

        def decode_part(part):
            charset = part.get_content_charset('utf-8')  
            email_body = part.get_payload(decode=True)
            try:
                return email_body.decode(charset, 'ignore')  
            except LookupError:  
                return email_body.decode('utf-8', 'ignore') 

        def find_verification_code(mail, current_email_address):
            result, data = mail.search(None, '(SUBJECT "your one-time code" FROM "Nike")')
            if result != 'OK':
                print("No emails found from Nike.")
                return None

            messages = data[0].split()
            if not messages:
                print("No new emails from Nike.")
                return None

            messages = sorted(messages, key=int, reverse=True)

            for latest_email_id in messages:
                result, data = mail.fetch(latest_email_id, '(RFC822)')
                if result != 'OK':
                    print(f"Could not fetch the email with ID {latest_email_id.decode('utf-8')}.")
                    continue

                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)
        
                to_address = email_message['To']
                if to_address and (current_email_address in to_address):
                    for part in email_message.walk():
                        if part.get_content_type() in ["text/plain", "text/html"]:
                            email_body = decode_part(part)
                            code_match = re.search(r"\b(\d{8})\b", email_body)
                            if code_match:
                                return code_match.group(1)

            print("Could not find a verification code in the emails for", current_email_address)
            return None


        def login_and_search(current_email_address):
            mail = imaplib.IMAP4_SSL(imap_url)
            mail.login(email_user, email_password)
            mail.select('inbox')

            emailVerifyToken = None
            max_attempts = 5

            for attempt in range(max_attempts):
                print(f"Attempt {attempt + 1}/{max_attempts}: Searching for the verification email for {current_email_address}.")
                emailVerifyToken = find_verification_code(mail, current_email_address)
                if emailVerifyToken:
                    print(f"Verification Code found for {current_email_address}: {emailVerifyToken}")
                    break
                else:
                    print(f"Verification email not found for {current_email_address}, waiting 10 seconds before retrying...")
                    time.sleep(10)

            mail.logout()
            return emailVerifyToken
        emailVerifyToken = login_and_search(emaill)

        driver.sleep(10)

        codeinp = driver.find_element(By.ID,'l7r-code-input')
        codeinp.write(str(emailVerifyToken))

        driver.sleep(3)
        finalclick = driver.find_element(By.ID,'privacyTerms')
        finalclick.click()

        driver.sleep(8)

        createacc = driver.find_element(By.CLASS_NAME,'nds-btn css-hj7pkf btn-primary-dark  btn-md')
        driver.sleep(5)
        createacc.click()

        driver.sleep(15)
        with open('accs.txt','a') as f:
            f.write(emaill+':'+passw+'\n')
        driver.get('https://www.nike.com/member/settings')
        driver.sleep(8)

        numadd = driver.find_element(By.CLASS_NAME,'nds-btn underline d-sm-ib css-92f2w3 ex41m6f0 cta-primary-dark underline')
        numadd.click()
        driver.sleep(6)

        agree = driver.find_element(By.ID,'agreeToTerms')
        agree.click()
        driver.sleep(2)


        js_code2 = """
        var selectElement = document.querySelector('select[name="callingCode"]');
        selectElement.value = '44_GB'; 

   
        var event = new Event('change', { 'bubbles': true, 'cancelable': true });
        selectElement.dispatchEvent(event);
    """
        driver.execute_script(js_code2)
        driver.sleep(5)


# Your 5sim API token
        token = ''

# API details for the purchase
        country = 'england'
        operator = 'virtual51'
        product = 'nike'

        domain = '5sim.net'
        headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
        }
        purchase_successful = False
        attempt_count = 0
        max_attempts = 3  # Max attempts to purchase number
        phone_num = None  # Variable to store the purchased phone number

    # Attempt to purchase number
        while not purchase_successful and attempt_count < max_attempts:
            print(f"Attempt {attempt_count + 1} to purchase number...")
            purchase_response = requests.get(f'https://{domain}/v1/user/buy/activation/{country}/{operator}/{product}', headers=headers)
            if purchase_response.status_code == 200:
                purchase_data = purchase_response.json()
                if 'phone' in purchase_data:
                    original_phone_num = purchase_data['phone']
            # Remove the +44 prefix from the phone number
                    phone_num = original_phone_num.replace('+44', '')
                    print(f"Number purchased successfully. Modified Phone Number: {phone_num}")
                    purchase_id = purchase_data['id']
                    purchase_successful = True
                else:
                    print("Purchase successful but phone number not found in response. Trying again...")
            else:
                print("Failed to purchase number. Trying again...")
            attempt_count += 1
            time.sleep(5)  # Wait 5 seconds before trying again

        if not purchase_successful:
            print("Failed to purchase number after several attempts. Exiting.")
            exit()

        phoneinp = driver.find_element(By.ID,'phoneNumber')
        phoneinp.write(phone_num)

        driver.sleep(8)

        sendcode = driver.find_element(By.CLASS_NAME,'nds-btn mr-12-sm css-1kvzham ex41m6f0 btn-primary-dark  btn-responsive')
        sendcode.click()
        driver.sleep(8)

        checks_done = 0
        max_checks = 25  # Max checks for SMS
        sms_received = False

        while checks_done < max_checks and not sms_received:
            print(f"Checking for SMS ({checks_done + 1}/{max_checks})...")
            check_sms_response = requests.get(f'https://{domain}/v1/user/check/{purchase_id}', headers=headers)
            if check_sms_response.status_code == 200:
                sms_data = check_sms_response.json()
                if sms_data.get('status') == 'RECEIVED' and sms_data.get('sms'):
                    phonesmscode = sms_data['sms'][0]['code']  # Get the code from the first SMS
                    print("SMS code received:", phonesmscode)
                    sms_received = True
                else:
                    print("No SMS received yet.")
            else:
                print("Failed to check SMS. Trying again...")
            checks_done += 1
            if not sms_received:
                time.sleep(5)  

        if not sms_received:
            print("Failed to receive SMS after several checks.")
        else:
    # Finish the order once the SMS code is received
            finish_response = requests.get(f'https://{domain}/v1/user/finish/{purchase_id}', headers=headers)
            if finish_response.status_code == 200:
                print("Order finished successfully.")
            else:
                print("Failed to finish the order.")

        inputcode = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/section/div/div[3]/form/div[1]/div[1]/input')
        inputcode.write(phonesmscode)
        driver.sleep(4)
        donebutton = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div/div/section/div/div[3]/form/div[2]/button')
        donebutton.click()
        driver.sleep(10)

        driver.quit()
        driver.close()

def chunk_it(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def main():
    max_browsers = 3  # Set this based on your needs

    # Load emails from file
    with open('emails.txt', 'r') as emails_file:
        email_lines = [email_line.strip() for email_line in emails_file.readlines()]

    email_chunks = chunk_it(email_lines, max_browsers)
    threads = []

    for chunk in email_chunks:
        t = threading.Thread(target=lambda c=chunk: [process_email(email) for email in c])
        threads.append(t)
        t.start()
        time.sleep(1)  # Delay between starting each thread/browser

    for thread in threads:
        thread.join()

    print("Finished processing all emails.")

if __name__ == "__main__":
    main()
