# Automated Sending Whatsapp Messages to saved numbers on your phone.

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

# driver.maximize_window()
# driver = webdriver.Chrome()

# code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # open chrome
driver.get('https://web.whatsapp.com/')

# resize windows
pyautogui.keyDown('win')
pyautogui.press('right')
pyautogui.keyUp('win')
# sleep(1)
pyautogui.press('enter')
# pyautogui.press('alt', 'tab')



for x in range(6):
    sleep(5)
    print(6 - x, end=', ')


def send_message(name):
    action = ActionChains(driver)
    search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    action.click(search).perform()
    action.send_keys(name).perform()
    action.send_keys(Keys.ENTER).perform()

    # textbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    # action.click(textbox).perform()
    
    message_array = ["Hacktoberfest is a global event with the main goal to raise awareness about Open Source and encourage as many developers as possible to participate regularly, not just in October. Hacktoberfest also comes with a challenge and invites participants to complete it. Participate in HacktoberFest and get a chance to redeem an official HacktoberFest 2022 T-shirt or get a tree planted in your name.",
                     " ",
                     "- What is Git/GitHub?",
                     "- What is open source?",
                     "- What is HacktoberFest?",
                     "- How to register for Hacktoberfest?",
                     "- How to find Repositories?",
                     "- How to create a pull request?",
                     "- Learn version control",
                     " ",
                     "Mark your Calendars: October 20, 2022 - 7:00 PM - 9:00 PM (PST GMT +5)",
                     "Register here: https://bit.ly/HacktoberFest-2022"
                     ]

    for x in message_array:
        action.send_keys(x).perform()
        ActionChains(driver).key_down(Keys.SHIFT).key_down(
            Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).perform()

    sleep(1)
    action.send_keys(Keys.ENTER).perform()

    search.clear()
    
    print('sent to ' + name)
    sleep(1)


# send_message("Name of the person")

names = ["Amaan PA", "Boiz", "Adam Saleem", "REMOTE CODERS"]

for n in names:
    send_message(n)

sleep(3)

driver.quit()

