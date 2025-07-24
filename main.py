from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Step 1: Open the website
driver = webdriver.Chrome()  # If chromedriver not in PATH, use executable_path="path/to/chromedriver"
driver.get("https://demoqa.com/buttons")
driver.maximize_window()

actions = ActionChains(driver)

# Step 2: Perform Mouse Actions

# 1. Double Click
double_click_btn = driver.find_element(By.ID, "doubleClickBtn")
actions.double_click(double_click_btn).perform()
print("✅ Double Clicked")

# 2. Right Click
right_click_btn = driver.find_element(By.ID, "rightClickBtn")
actions.context_click(right_click_btn).perform()
print("✅ Right Clicked")

# 3. Single Click (Click Me button)
single_click_btn = driver.find_element(By.XPATH, "//button[text()='Click Me']")
actions.click(single_click_btn).perform()
print("✅ Single Clicked")

time.sleep(3)  # Pause to observe
driver.quit()
