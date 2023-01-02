import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

# C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\GDSC\Resources\Zselenium\chromedriver.exe"

options = webdriver.ChromeOptions()

profile = "C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")

driver = webdriver.Chrome(options=options, use_subporcess=True)
driver.get("https://web.whatsapp.com/")
print("Opened Whatsapp")

wait = 13

for i in range(wait):
    print(wait - i, end=", ")
    sleep(2)
print('\n')


def send_whatsapp_message(name, message):
    search = driver.find_element(
        By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    search.click()
    search.clear()

    search.send_keys(name)
    search.send_keys(Keys.ENTER)

    # textbox = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

    for x in message:
        textbox.send_keys(x)
        ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(
            Keys.SHIFT).perform()

    sleep(1)
    textbox.send_keys(Keys.ENTER)

    print("Sent to: " + name)


long_message = '''Hacktoberfest is a global event with the main goal to raise awareness about Open Source and encourage as many developers as possible to participate regularly, not just in October. Hacktoberfest also comes with a challenge and invites participants to complete it. Participate in HacktoberFest and get a chance to redeem an official HacktoberFest 2022 T-shirt or get a tree planted in your name.
- What is Git/GitHub?
- What is open source?
- What is HacktoberFest?
- How to register for Hacktoberfest?
- How to find Repositories?
- How to create a pull request?
- Learn version control
Mark your Calendars: October 20, 2022 - 7:00 PM - 9:00 PM (PST GMT +5)
Register here: https://bit.ly/HacktoberFest-2022'''

my_message = list(long_message.split('\n'))

names = "Amaan PA"

name_list = ['Amaan PA', 'Adam Saleem', 'Boiz']

for nam in name_list:
    send_whatsapp_message(nam, my_message)


for i in range(20):
    print(i, end=", ")
    sleep(2)
