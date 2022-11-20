# Automating event posting on social media platforms.

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

username = "umtgdsc@gmail.com"  # FB Email Address
fb_pass = "gdsc@umt_fb"        # FB Password


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver.maximize_window()
# driver = webdriver.Chrome()

# code to stop window from closing
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")

chrome_options.add_experimental_option("detach", True)

webfb = webdriver.Chrome(options=chrome_options)  # open chrome
webfb.get('https://www.facebook.com/')

# resize windows
# pyautogui.keyDown('win')
# pyautogui.press('right')
# pyautogui.keyUp('win')
# sleep(1)
# pyautogui.press('enter')
# pyautogui.press('alt', 'tab')

sleep(2)

webfb.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
webfb.find_element(By.XPATH, '//*[@id="pass"]').send_keys(fb_pass)
login_button = webfb.find_element(By.NAME, 'login')
login_button.click()


print("12 Timer: ")
for x in range(12):
    sleep(1)
    print(12 - x, end=', ')

sleep(3)

message = "Hello!\nThis is an Automated message! \n This is the way you automate a message"

fb_logo = webfb.find_element(
    By.CLASS_NAME, 'x1ujvgzy')

action = ActionChains(webfb)
action.click(fb_logo).perform()
sleep(3)

# for i in range(11):
#     print(i, end=', ')
#     # pyautogui.press('tab')
#     # ActionChains(webfb).key_down(Keys.TAB).perform()
#     fb_logo.send_keys


action.send_keys(Keys.TAB * 13)
action.perform()

sleep(1)
# ActionChains(webfb).key_down(Keys.ENTER).perform()
action.send_keys(Keys.ENTER).perform()

sleep(7)
action.send_keys("Hello! How are you all doing.\n Its been a while since we have uploaded, but get ready to have an amazing road ahead.\n Amaan Majeed Siging off").perform()
# action = ActionChains(webfb)

# action.send_keys("Hello! How are you brother!")
# action.perform()


for j in range(11):
    ActionChains(webfb).key_down(Keys.TAB).perform()

# simply press enter or uncomment the line below to complete the automation. 😇
# action.send_keys(Keys.ENTER).perform()

print('done')
