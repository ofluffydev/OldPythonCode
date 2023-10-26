import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Start the browser
driver = webdriver.Chrome()

# Load the website
driver.get("https://deltamath.com/")

# Take a screenshot of the website
driver.save_screenshot("screenshot.png")

#User input to say they are ready to continue
input("Press enter to continue...")

#Remove screenshot when done
file_path = "/mnt/chromeos/MyFiles/Code/Coding/Python/messingAround/screenshot.png"
try:
    os.remove(file_path)
    print(f"{file_path} successfully deleted.")
except OSError as e:
    print(f"Error: {file_path} - {e.strerror}.")
