# Automating event posting on social media platforms.

from selenium import webdriver
from selenium.webdriver.common.by import By # for xpath
from selenium.webdriver.chrome.options import Options # stop closing
from time import sleep

# driver.maximize_window()
# driver = webdriver.Chrome()

# code to stop window from closing
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

webfb = webdriver.Chrome(options=chrome_options) # open chrome
webfb.get('https://www.facebook.com/')

sleep(1)

username = "umtgdsc@gmail.com"
fb_pass = "gdsc@umt_fb"
insta_pass = "gdsc@umt_cs"
linkedin_pass = "gdsc@umt_ln"

webfb.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
webfb.find_element(By.XPATH, '//*[@id="pass"]').send_keys(fb_pass)
login_button = webfb.find_element(By.NAME, 'login')
login_button.click()

sleep(10)
message = "Hello!\nThis is an Automated message! \n This is the way you automate a message"
post_button = webfb.find_element(By.XPATH, '//*[@id="mount_0_0_qe"]/div/div[1]/div/div[5]/div/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span')
post_button.click()



sleep(10)

print('done')
