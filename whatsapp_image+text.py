# Automated Sending Whatsapp Messages to saved numbers on your phone.

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import pyautogui

# driver.maximize_window()
# driver = webdriver.Chrome()

# open file explorer and go to
# C:\Program Files\Google\Chrome\Application
# open cmd in the location bar, and paste the command below, where dir = "The location of your chrome webdriver"
# chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\GDSC\Resources\Zselenium\chromedriver.exe

# code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(options=chrome_options)  # open chrome
driver.get('https://web.whatsapp.com/')


# Shift windows
pyautogui.hotkey('alt', 'tab')


# Algo to wait for the page to open and then immediately start execution
count = 0
while True:
    try:
        search = driver.find_element(
            By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]').click()
    except:
        count = count + 2
        print(count)
        sleep(2)
        continue
    break


def send_message(name, message):
    search = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search.click()
    search.send_keys(name)
    search.send_keys(Keys.ENTER)

    textbox = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

    textbox.click()
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'v')

    sleep(1.5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')))
    picbox = driver.find_element(
        By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[1]/div[3]/div/div/div[2]/div[1]/div[1]/p')

    for x in message:
        picbox.send_keys(x)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
            Keys.SHIFT).perform()

    sleep(1.5)
    # action.send_keys(Keys.ENTER).perform()
    picbox.send_keys(Keys.ENTER)

    search.clear()

    print('sent to ' + name)
    sleep(0.3)


long_message = '''multi-line message'''


# send_message("Name of the person")
names = ['person1', 'person2', 'person3']

my_message = list(long_message.split('\n'))

for nam in names:
    send_message(nam, my_message)

print("Done")
sleep(10)

# driver.quit()
