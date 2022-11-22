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
driver.get('https://www.google.com/')

# resize windows
pyautogui.keyDown('win')
pyautogui.press('right')
pyautogui.keyUp('win')
sleep(0.5)
pyautogui.press('enter')
# pyautogui.press('alt', 'tab')

action = ActionChains(driver)


# Hacktoberfest is a global event with the main goal to raise awareness about Open Source and encourage as many developers as possible to participate regularly, not just in October. Hacktoberfest also comes with a challenge and invites participants to complete it. There are exciting rewards in return including an amazing official swag kit.
# - What is Git/GitHub?
# - What is open source?
# - What is HacktoberFest?
# - How to register for Hacktoberfest?
# - How to find Repositories?
# - How to create a pull request?
# - Learn version control
# 📌Mark your Calendars: October 20, 2022 - 7: 00 PM - 9: 00 PM(PST GMT + 5)


search = driver.find_element(
    By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')

for n in range(2):
    search.clear()
    search.click()
    action.key_down(Keys.CONTROL)
    action.send_keys("v")
    action.key_up(Keys.CONTROL)
    action.perform()
    sleep(2)


print("done")
sleep(3)

# driver.quit()
