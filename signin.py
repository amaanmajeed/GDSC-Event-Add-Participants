import subprocess
import sys

def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


packages = ['undetected-chromedriver', 'selenium']

for package in packages:
    install(package)
    print('\n')

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
remote_debugging_port = "5454"
user_data_dir = "D:\GDSC\Resources\Zselenium\chromedriver.exe"

cmd = [chrome_path, "--remote-debugging-port=" +
       remote_debugging_port, "--user-data-dir=" + user_data_dir]
subprocess.Popen(cmd)
