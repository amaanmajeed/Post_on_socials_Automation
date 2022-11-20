# Automating LinkedIn, so it logins and posts automatically.

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

username = "umtgdsc@gmail.com"  # FB Email Address
password = "***********"        # LinkedIn Password

# code to stop window from closing
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

chrome_options.add_experimental_option("detach", True)

webln = webdriver.Chrome(options=chrome_options)  # open chrome
webln.get('https://www.linkedin.com/')

sleep(1)
# resize windows
pyautogui.keyDown('win')
pyautogui.press('right')
pyautogui.keyUp('win')
sleep(0.5)
pyautogui.press('enter')
# pyautogui.press('alt', 'tab')

for x in range(5):
    print(5 - x, end=', ')
    sleep(1)

lname = webln.find_element(By.NAME, 'session_key')
lpass = webln.find_element(By.NAME, 'session_password')
login_button = webln.find_element(
    By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/button')

lname.send_keys(username)
lpass.send_keys(password)
print("Sent Credentials")

action = ActionChains(webln)
action.click(login_button).perform()
print("login complete")

sleep(1)


action.send_keys(Keys.TAB * 2).perform()
action.send_keys(Keys.ENTER).perform()
action.send_keys(Keys.TAB * 2).perform()
action.send_keys(Keys.ENTER).perform()
print("Entered into TextField")
sleep(2)

message = "Hello!\nThis is an Automated message! \n This is the way you automate a message"
action.send_keys(message)

action.send_keys(Keys.TAB * 9).perform()
sleep(0.2)
action.send_keys(Keys.TAB).perform()

# action.send_keys(Keys.ENTER).perform()

print("done")
