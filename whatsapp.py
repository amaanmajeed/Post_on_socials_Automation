# Automated Sending Whatsapp Messages to saved numbers on your phone.

from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# driver.maximize_window()
# driver = webdriver.Chrome()

# code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)  # open chrome
driver.get('https://web.whatsapp.com/')


for x in range(6):
    sleep(5)
    print(6 - x)


def send_message(name):
    search = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search.click()
    search.send_keys(name)
    search.send_keys(Keys.ENTER)

    textbox = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    textbox.send_keys("Hacktoberfest is a global event with the main goal to raise awareness about Open Source and encourage as many developers as possible to participate regularly, not just in October. Hacktoberfest also comes with a challenge and invites participants to complete it. Participate in HacktoberFest and get a chance to redeem an official HacktoberFest 2022 T-shirt or get a tree planted in your name.")
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- What is Git/GitHub?")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- What is open source?")

    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- What is HacktoberFest?")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- How to register for Hacktoberfest?")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- How to find Repositories?")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- How to create a pull request?")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("- Learn version control")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("Mark your Calendars: October 20, 2022 - 7:00 PM - 9:00 PM (PST GMT +5)")
    
    ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).perform()
    ActionChains(driver).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
    textbox.send_keys("Register here: https://bit.ly/HacktoberFest-2022")
    textbox.send_keys(Keys.ENTER)

    search.clear()
    
    print('sent to ' + name)
    sleep(2)


# send_message("Name of the person")

send_message("Amaan")
send_message("Ahmed")
send_message("Ali")
send_message("Salman")

sleep(3)

driver.quit()

