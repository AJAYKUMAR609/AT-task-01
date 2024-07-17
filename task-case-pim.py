
#task-01 login to orange hrm portal
import os
import time
import app
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



# Open the OrangeHRM login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


# Set an explicit wait of 10 seconds
wait = WebDriverWait(driver, 10)

# Log in with valid credentials
username_input = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
username_input.send_keys("Admin")

password_input = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_input.send_keys("admin123")

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
first_name_input.send_keys("keerthi")  # Replace with the actual first name

middle_name_input = driver.find_element(By.NAME, "middleName")
middle_name_input.send_keys("Ajay")  # Replace with the actual middle name

last_name_input = driver.find_element(By.NAME, "lastName")
last_name_input.send_keys("KUMAR")  # Replace with the actual last name
#

# Save the employee details
save_button = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")))
save_button.click()



#employee_id_input = WebDriverWait(driver, 10).until(
  #  EC.presence_of_element_located((By.XPATH, "your-correct-xpath-here"))


# add license number
driver.find_element((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))


#add license expiry
#license_expiry_date_input=wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR,("input#class=oxd-input oxd-input--active")))

#license_expiry_date_input.send_keys("2334")
#add nationality
nationality_input=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]")
nationality_input.send_keys("indian")
#matrial status
marital_status_input=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]")
marital_status_input.send_keys("unmarried")
#date of birth
date_of_birth_input=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input")
date_of_birth_input.send_keys("1996-01-13")
#
gender_button=driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label")
gender_button.send_keys("male").click()
#
