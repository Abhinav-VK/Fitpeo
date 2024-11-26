from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

def automate_fitpeo():
    try:
        print("Starting automation...")
        
        # Initialize the WebDriver with headless mode
        driver = webdriver.Chrome()
        
        print("Navigating to FitPeo homepage...")
        driver.get("https://www.fitpeo.com/")
        driver.maximize_window()
        
        print("Waiting for Revenue Calculator page to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Revenue Calculator"))
        )
        
        revenue_calculator = driver.find_element(By.LINK_TEXT, "Revenue Calculator")
        revenue_calculator.click()
        
        print("Scrolling down to slider section...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        print("Adjusting slider to value 820...")
        slider = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='range']"))
        )
        
        # Adjust slider value directly
        slider_value = slider.get_attribute('max')
        #print("Sliderrrrr " + slider_value)
        slider_value = str(int(float(slider_value)) * 820 / 200)
        slider.send_keys(slider_value)
        #driver.implicitly_wait(20)
        
        print("Updating text field...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ":r0:"))
        ).send_keys("560")
        
        print("Validating slider value...")
        actual_slider_value = slider.get_attribute('value')
        assert float(actual_slider_value) == 820, f"Expected slider value 820, but got {actual_slider_value}"
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Close the browser
        driver.close()

if __name__ == "__main__":
    automate_fitpeo()
