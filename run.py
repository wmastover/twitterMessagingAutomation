from webdriver_manager.chrome import ChromeDriverManager
import time 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from readCSV import readCSV
import pyautogui
from saveAsCSV import saveAsCSV
from twitterLogon import twitterLogon

def twitterNewline():
    # Hold ShiftKey
    pyautogui.keyDown('shift')

    # Press Enter
    pyautogui.press('enter')

    # Release the Shift key
    pyautogui.keyUp('shift')

    pyautogui.keyDown('shift')

    # Press Enter
    pyautogui.press('enter')

    # Release the Shift key
    pyautogui.keyUp('shift')


array = readCSV("accounts.csv")

chromedriver = ChromeDriverManager().install()


# chrome_options = Options()
# # chrome_options.add_argument("user-data-dir=/Users/will/Library/Application Support/Google/Chrome/") # Path to your chrome user data
# chrome_options.add_argument("profile-directory=Profile 2") # Your profile directory
# chrome_options.add_argument("--no-sandbox") 
# chrome_options.add_argument("--disable-dev-shm-usage")

webdriver_service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=webdriver_service)


twitterLogon("js5668301@gmail.com", "SecondBrainAnna",  "Frontdoor2023", driver)

accountName = "anna"

ouputArray = []

for row in array:
    try:
        driver.get(row[0])
        time.sleep(10)

        # try:
        DMElement = driver.find_element(By.XPATH, '//div[@data-testid="sendDMFromProfile"]')
        DMElement.click()
        time.sleep(40)

        messageBar = driver.find_element(By.XPATH, "//*[@data-testid='dmComposerTextInput']")
        
        messageBar.click()

        pyautogui.typewrite(row[1])

        twitterNewline()

        pyautogui.typewrite("I also noticed that you're into curating content and exploring knowledge in the tech sphere.")

        twitterNewline()

        pyautogui.typewrite("I built a GPT-4 powered tool to automatically organise your bookmarks and explore a hand-curated db of tech knowledge from some of the best builders around. ")

        twitterNewline()

        pyautogui.typewrite("We're looking for people passionate about tech to try it out and explore - you seem like a great fit and I'd love to share access! Hit me back if you're interested.")

        sendButton = driver.find_element(By.XPATH, "//*[@data-testid='dmComposerSendButton']")

        time.sleep(1)

        sendButton.click( )

        ouputArray.append([row[0],row[1], accountName])

        time.sleep(3)


    except:
        print("error")
        ouputArray.append([row[0],row[1], "Not Sent"])


    saveAsCSV(ouputArray, "outputArray.csv")

    
    # except:
    #     print("error")


