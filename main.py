# Automating Form Submit for GDSC UMT - Member's page

from selenium import webdriver
from selenium.webdriver.common.by import By #for xpath
from selenium.webdriver.chrome.options import Options #stop closing
from time import sleep

# driver.maximize_window()
# driver = webdriver.Chrome()

#code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

web = webdriver.Chrome(options=chrome_options) # open chrome
web.get('https://forms.gle/mGic4DZ9aStCjsu49')
sleep(1)

name = "Automated testing"
email = "automation@test.com"
ph = "03123456789"
intro = "This is an Automated message"

namepath = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
emailpath = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
phpath = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
intropath = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
submitpath = web.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')


namepath.send_keys(name)
emailpath.send_keys(email)
phpath.send_keys(ph)
intropath.send_keys(intro)
sleep(3)
# submitpath.click()


print('done')
