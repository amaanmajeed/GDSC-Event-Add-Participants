import undetected_chromedriver as webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By  # for xpath
from selenium.webdriver.chrome.options import Options  # stop closing
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import csv
import subprocess

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
remote_debugging_port = "5454"
user_data_dir = "D:\GDSC\Resources\Zselenium\chromedriver.exe"

cmd = [chrome_path, "--remote-debugging-port=" +
       remote_debugging_port, "--user-data-dir=" + user_data_dir]
subprocess.Popen(cmd)
