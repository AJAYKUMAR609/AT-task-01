import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Set an explicit wait of 10 seconds
wait = WebDriverWait(driver, 10)

#ak

# Log in with valid credentials (you can modify this part)
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_input.send_keys("Admin")  # Replace with the actual username

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys("admin123")  # Replace with the actual password

login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button")))
login_button.click()

# Navigate to the PIM module
pim_module_link = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")))
pim_module_link.click()

# Click on 'Add Employee'
add_employee_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")))
add_employee_button.click()

# Fill in employee details
first_name_input = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
first_name_input.send_keys("keer")  # Replace with the actual first name

middle_name_input = driver.find_element(By.NAME, "middleName")
middle_name_input.send_keys("ram")  # Replace with the actual middle name

last_name_input = driver.find_element(By.NAME, "lastName")
last_name_input.send_keys("KUMAR")  # Replace with the actual last name
#

# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")))
save_button.click()

driver.quit()