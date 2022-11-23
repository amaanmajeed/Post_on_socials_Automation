# Automating Facebook Page so it logins and posts

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui

username = "umtgdsc@gmail.com"  # FB Email Address
fb_pass = "************"        # FB Password


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver.maximize_window()
# driver = webdriver.Chrome()
def post_on_fb(message):
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")

    chrome_options.add_experimental_option("detach", True)

    webfb = webdriver.Chrome(options=chrome_options)  # open chrome

    # code to stop window from closing
    webfb.get('https://www.facebook.com/')
    sleep(2)

    webfb.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
    webfb.find_element(By.XPATH, '//*[@id="pass"]').send_keys(fb_pass)
    login_button = webfb.find_element(By.NAME, 'login')
    login_button.click()

    print("7 Timer: ")
    for x in range(7):
        sleep(1)
        print(7 - x, end=', ')

    sleep(3)
    fb_logo = webfb.find_element(By.CLASS_NAME, 'x1ujvgzy')

    action = ActionChains(webfb)
    action.click(fb_logo).perform()
    sleep(3)

    action.send_keys(Keys.TAB * 14)
    action.perform()

    sleep(1)
    action.send_keys(Keys.ENTER).perform()

    sleep(9)
    action.send_keys(message).perform()

    action.send_keys(Keys.TAB * 11)
    action.perform()

# simply press enter or uncomment the line below to complete the automation. 😇
# action.send_keys(Keys.ENTER).perform()

message = "Hello! How are you all doing.\n Its been a while since we have uploaded, but get ready to have an amazing road ahead.\n Amaan Majeed Siging off"

post_on_fb(message)

print('done')
