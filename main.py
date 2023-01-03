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

driver = webdriver.Chrome(options=options, use_subporcess=True)
# add link here
driver.get("add your link here,which has the add Attendee button")
print("Opened link")

wait = 6
for i in range(wait):
    print(wait - i, end=", ")
    sleep(2)
print('\n')

currentcount = 0
headcount = 0

while True:
    try:
        # Change name of file here, and put in the same folder
        with open('C:\\Users\\Hp\\Documents\\Git\\Add Participants\\file.csv', 'r') as f:
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
                cancel_btn = driver.find_element(
                    By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[1]/button').click()

                # send_btn = driver.find_element(
                #     By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[2]/div/button').click()

                sleep(3)
                print("First Name: " + str(row[0]) + "   Last Name: " + str(row[1]) + "   Head Counter: " + str(headcount) +
                      "   Current Counter: " + str(currentcount))
                
                currentcount = currentcount + 1
                headcount = headcount + 1

    except:
        print("Error Occured")
        try:
            cancel_btn = driver.find_element(By.XPATH, '//*[@id="overlay-container"]/div/div/div[2]/form/div/div[7]/div/div[1]/button')
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
