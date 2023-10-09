from time import sleep

import requests
from selenium import webdriver

# TODO ask dev team how to inject token
print("Open Driver")
driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")

print("Get token via API")
payload = "username=Admin&password=admin123"
headers = dict(Cookie="orangehrm=7f9fc5f76bce76d2049aa17e4c98578e")
req = requests.post(
    "https://opensource-demo.orangehrmlive.com/web/index.php/auth/validate",
    data=payload,
    headers=headers,
)

token = req.cookies["orangehrm"]
print(token)
sleep(2)

# Try to inject token as cookie
print("Execute script to inject token")
cookie_script = f'document.cookie = "orangehrm={token}; path=/web; secure; HttpOnly;"'
driver.execute_script(cookie_script)

# Refresh
sleep(2)
print("Refresh")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

sleep(100)
