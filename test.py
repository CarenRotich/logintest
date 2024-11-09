from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

# Path to geckodriver
geckodriver_path = "C:/Users/smrc/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe"

# Set up the Firefox driver service
service = Service(geckodriver_path)

# Optional: Set Firefox options (e.g., headless mode)
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Uncomment to run in headless mode (no browser window)

# Set up the Firefox WebDriver
driver = webdriver.Firefox(service=service, options=firefox_options)

# Step 1: Open the login page
driver.get("http://lynne.infinityfreeapp.com/login.php")

# Step 2: Locate the login form elements
username_field = driver.find_element(By.NAME, "email")  # Update 'email' to the correct name attribute
password_field = driver.find_element(By.NAME, "password")  # Update 'password' to the correct name attribute
sign_in_button = driver.find_element(By.NAME, "submit")  # Update to the correct button name

# Step 3: Interact with the form elements
username_field.send_keys("karenrotich97@gmail.com")  # Replace with your test username
password_field.send_keys("123456")  # Replace with your test password
sign_in_button.click()  # Click the sign-in button

# Step 4: Wait for the page to load (simple wait)
driver.implicitly_wait(5)  # Wait for 5 seconds (you can adjust as needed)

# Step 5: Capture test results
test_result = "Login Failed"  # Default result is failure

try:
    # Look for the login success message in the alert-success div
    login_success_message = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success")
    test_result = "Login Successful"  # Update the result if login is successful
    result_message = login_success_message.text.strip()  # Get the success message text
except Exception as e:
    result_message = str(e)

# Save the result to a file
with open("test_results.txt", "a") as result_file:
    result_file.write(f"Test Result: {test_result}\n")
    result_file.write(f"Result Message: {result_message}\n")
    result_file.write(f"Test Date and Time: {time.ctime()}\n")
    result_file.write("-" * 50 + "\n")

# Step 6: Close the browser
driver.quit()

print(f"Test Result: {test_result}")
print(f"Result Message: {result_message}")
