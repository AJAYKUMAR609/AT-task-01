

#task-labour.gov.in to download monthly reports

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://labour.gov.in/")
time.sleep(5)

# Find the link to the monthly progress report
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
actions = ActionChains(driver)
actions.move_to_element(documents_menu).perform()
time.sleep(3)
monthly_report_link = driver.find_element(By.LINK_TEXT, "Monthly Progress Report")
monthly_report_url = monthly_report_link.get_attribute("href")

# Make a request to download the report
report_response = requests.get(monthly_report_url)
with open(r"C:\Users\ajayk\OneDrive\Desktop\python1\Monthly_Progress_Report.pdf", "wb") as file:
    file.write(report_response.content)

print("Monthly progress report downloaded successfully")


#task-labour.gov.in for photos

import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajayk\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://labour.gov.in/")
time.sleep(5)

# Go to media menu and photo gallery
driver.find_element(By.LINK_TEXT, "Media").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT, "Click for more info of Press Releases").click()
driver.find_element(By.LINK_TEXT, "Photo Gallery").click()
time.sleep(5)

# Create the photo folder if it doesn't exist
photo_folder = r"C:\Users\ajayk\OneDrive\Desktop\python1\Photo Gallery"
if not os.path.exists(photo_folder):
    os.makedirs(photo_folder)

# Get all image elements
photos = driver.find_elements(By.CSS_SELECTOR, "img")[:10]

# Download and save images
for index, photo in enumerate(photos):
    photo_url = photo.get_attribute("src")
    photo_response = requests.get(photo_url)
    with open(os.path.join(photo_folder, f"photo_{index + 1}.jpg"), "wb") as file:
        file.write(photo_response.content)
        print(f"Downloaded photo {index + 1}")

print("Photo download is complete!")

###task-for opening guvi insta-page and showing the no of followers
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.instagram.com/guviofficial/")
time.sleep(10)  # Add a delay to allow page content to load

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
followers_element = wait.until(EC.presence_of_element_located((By.XPATH, "//html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button")))
following_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button")))

# Extract the follower and following counts
followers_count = followers_element.get_attribute("title")
following_count = following_element.text

print(f"Followers: {followers_count}")
print(f"Following:{following_count}")

# Quit the WebDriver
driver.quit()


#task-21-for
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.by import By
# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.saucedemo.com/inventory.html")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()

# Step 4: Get cookies after login
time.sleep(2)  # Wait for the page to load
cookies_after_login = driver.get_cookies()
print("\nCookies after login:")
for cookie in cookies_after_login:
    print(f"{cookie['name']}: {cookie['value']}")

# Step 5: Verify cookies (you can add custom verification logic here)

# Step 6: Log out (if applicable)
# Example: driver.find_element_by_id("logout-button").click()

# Clean up
driver.quit()

#task-11
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://jqueryui.com/droppable/")

# Switch to the iframe containing the draggable elements
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Locate the draggable element (white box)
draggable_element = driver.find_element(By.ID, "draggable")

# Locate the droppable element (yellow box)
droppable_element = driver.find_element(By.ID, "droppable")

# Perform the drag-and-drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Verify that the drop was successful
drop_success_text = droppable_element.find_element(By.TAG_NAME, "p").text
if "Dropped!" in drop_success_text:
    print("Drop was successful")
else:
    print("Drop failed")

# Clean up
driver.quit()











