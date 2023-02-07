import undetected_chromedriver as webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep
import csv


# C:\Program Files\Google\Chrome\Application
# chrome.exe --remote-debugging-port=8989 --user-data-dir="D:\GDSC\Resources\Zselenium\chromedriver.exe

options = webdriver.ChromeOptions()

profile = "C:\\Users\\Hp\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1"
options.add_argument(f"user-data-dir={profile}")
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=options, use_subporcess=True)
# add link here
driver.get(
    "https://gdsc.community.dev/accounts/dashboard/#/chapter-1857/event-47909/manage")
print("Opened link")

count = 0
while True:
    try:
        search = driver.find_element(
            By.XPATH, '//*[@id="react-main-dashboard-root"]/div/div[3]/div/div/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div/div[2]/button')
    except:
        count = count + 2
        print(count)
        sleep(2)
        continue
    break

currentcount = 0
headcount = 0

while True:
    try:
        # Change name of file here, and put in the same folder
        with open('C:\\Users\\Hp\\Documents\\Git\\Add Participants\\blockchain.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if (currentcount != headcount):
                    currentcount = currentcount + 1
                    continue

                if (row[0] == ""):
                    row[0] = "M"        # if entry is blank, replace it with M
                if (row[1] == ""):
                    row[1] = "M"

                add_btn = driver.find_element(
                    By.CLASS_NAME, 'add-attendee-button')
                add_btn.click()

                sleep(0.5)

                fname = driver.find_element(By.NAME, 'first_name')
                fname.send_keys(row[0])

                lname = driver.find_element(By.NAME, 'last_name')
                lname.send_keys(row[1])

                email = driver.find_element(By.NAME, 'email')
                email.send_keys(row[2])

                checkinbtn = driver.find_element(
                    By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[4]/div/label/span[1]/span[1]/input')
                checkinbtn.click()

                sleep(0.5)
                # cancel_btn = driver.find_element(
                #     By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[1]/button').click()

                send_btn = driver.find_element(
                    By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[2]/div/button').click()

                sleep(3)
                print(str(headcount + 1) + ". " +
                      str(row[0]) + " " + str(row[1]) + "\t        Email: " + str(row[2]))

                currentcount = currentcount + 1
                headcount = headcount + 1

    except:
        print("-----Entry Already present-----")
        try:
            cancel_btn = driver.find_element(
                By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[1]/button')
            cancel_btn.click()
        finally:
            sleep(1)
            currentcount = 0
            continue
    break

# email.send_keys(Keys.ENTER)

wait = 15
for i in range(wait):
    print(wait - i, end=", ")
    sleep(2)
print('\n')
