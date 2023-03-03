import subprocess

chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
remote_debugging_port = "5454"
user_data_dir = "D:\GDSC\Resources\Zselenium\chromedriver.exe"

cmd = [chrome_path, "--remote-debugging-port=" +
       remote_debugging_port, "--user-data-dir=" + user_data_dir]
subprocess.Popen(cmd)
