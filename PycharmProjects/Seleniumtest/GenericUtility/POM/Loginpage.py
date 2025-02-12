from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Loginpage:
    # Locator for the mobile number field
    element = (By.XPATH, "//input[@name='mobile']")

    def __init__(self, driver):
        self.driver = driver

    def performLogin(self, text):
        # Unpack the tuple to pass two separate arguments (By.XPATH, value)
        mobilenum = self.driver.find_element(*self.element)  # Unpacking the tuple
        mobilenum.send_keys(text)  # Send the text to the username input field
