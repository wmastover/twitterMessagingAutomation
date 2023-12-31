import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


def twitterLogon(email, username, password, driver):

    driver.get("https://twitter.com/login")
    time.sleep(20)

    emailLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Phone, email address, or username')]/ancestor::label[1]")

    emailInput = emailLabel.find_element( By.XPATH, ".//input[1]")

    emailInput.send_keys(email)

    time.sleep(1)

    nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

    nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

    nextButton.click()

    time.sleep(5)

    try:
        # Check if the page is the phone number page
        title = driver.find_element(By.XPATH, "//span[contains(text(), 'Enter your phone number or username')]")
        
        print("enter phone number or username found")

        # Input username
        usernameInput = driver.find_element(By.TAG_NAME, "input")

        usernameInput.send_keys(username)

        time.sleep(1)

        # Click next button
        nextButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

        nextButton = nextButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

        nextButton.click()



    except:
        print("phone number / username not requested")

    time.sleep(5)

    # Enter password
    passwordLabel = driver.find_element(By.XPATH, "//span[contains(text(), 'Password')]/ancestor::label[1]")

    passwordInput = passwordLabel.find_element( By.XPATH, ".//input[1]")

    passwordInput.send_keys(password)

    time.sleep(1)

    # click login

    LoginButtonText = driver.find_element(By.XPATH, "//span[contains(text(), 'Log in')]")

    LoginButton = LoginButtonText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

    LoginButton.click()


    # Accept terms and conditions 

    time.sleep(3)

    AcceptAllText = driver.find_element(By.XPATH, "//span[contains(text(), 'Accept all cookies')]")

    AcceptAllButton = AcceptAllText.find_element(By.XPATH, ".//ancestor::div[@role='button'][1]")

    AcceptAllButton.click()

    time.sleep(3)


# Test Data

# from webdriver_manager.chrome import ChromeDriverManager

# chromedriver = ChromeDriverManager().install()

# webdriver_service = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(service=webdriver_service)



# twitterLogon("wmabetting@gmail.com", "FrontdoorWill",  "Frontdoor2023", driver)


# Alternate account

# twitterLogon("js5668301@gmail.com", "SecondBrainAnna",  "Frontdoor2023", driver)