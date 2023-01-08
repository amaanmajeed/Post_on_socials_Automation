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

# open file explorer and go to
# C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\GDSC\Resources\Zselenium\chromedriver.exe

name_list = [
    'list of names you want to forward message to..'
]

# code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(options=chrome_options)  # open chrome
driver.get('https://web.whatsapp.com/')


wait = 7
for i in range(wait):
    print(wait - i, end=", ")
    sleep(2)
print('\n')

count = 0


def inc_count(countno):
    global count
    if (countno < len(name_list)):
        pyname(name_list[countno])
        count = count + 1


def pyname(name):
    namebox = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]')
    namebox.send_keys(name)
    namebox.click()
    # pyautogui.write(name, interval=0.03)
    sleep(1)
    # pyautogui.press('enter')
    namebox.send_keys(Keys.ENTER)
    namebox.clear()
    namebox.click()
    print(str(count) + '. sent to ' + name)
    sleep(0.3)


def forward_message():
    global count
    search = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search.click()
    search.clear()
    search.send_keys("The account you want the message to be forwarded from")
    search.send_keys(Keys.ENTER)

    sleep(1.5)

    forward_btn = driver.find_element(
        By.CLASS_NAME, 'r83rrh3w')

    forward_btn.click()
    sleep(1)

    namebox = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div/div[2]/div/div[2]')
    if (count < len(name_list)):
        namebox.send_keys("Dummy")
        namebox.click()
        # pyautogui.write(name, interval=0.03)
        sleep(1)
        # pyautogui.press('enter')
        namebox.clear()
        namebox.click()

        inc_count(count)
        inc_count(count)
        inc_count(count)
        inc_count(count)

        print("-------")

    with pyautogui.hold('shift'):
        pyautogui.press(['tab', 'tab', 'tab', 'tab'])

    # pyautogui.keyDown('shift')
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.press('tab')
    # pyautogui.keyUp('shift')
    sleep(1)
    pyautogui.press('enter')


# forward_message("Name of the person")

while (count < len(name_list)):
    forward_message()
print("Global count = " + str(count))

# driver.quit()
