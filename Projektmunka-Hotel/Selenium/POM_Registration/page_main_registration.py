from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Selenium.POM_general.browser_config import get_driver
from Selenium.POM_general.general_model import GeneralPage

URL ="localhost:4200"

class ReactFormPage(GeneralPage):
    def __init__(self,browser_type):
        browser = get_driver(browser_type)
        super().__init__(browser, URL)

    def button_register(self):
        button_register = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//a[text()="Register"]')))
        return button_register

    def input_firstname(self):
        input_firstname = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, 'firstName')))
        return input_firstname

    def input_firstname_check(self):
        try:
            input_firstname_check = self.browser.find_element(By.ID, 'firstName')
            return input_firstname_check
        except Exception:
            return None

    def input_lastname(self):
        input_lastname = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "lastName")))
        return input_lastname

    def input_phone(self):
        input_phone = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "phoneNumber")))
        return input_phone

    def input_email(self):
        input_email = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "email")))
        return input_email

    def input_password(self):
        input_password = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "password")))
        return input_password

    def input_zip_code(self):
        input_zip_code = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "zipcode")))
        return input_zip_code

    def input_city(self):
        input_city = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "city")))
        return input_city

    def input_address(self):
        input_address = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "address")))
        return input_address

    def dropbar_role(self):
        dropbar_role = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.ID, "role")))
        return dropbar_role

    def dropbar_beekeeper(self):
        dropbar_beekeeper = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH,"//select[@id='role']/option[contains(text(), 'Beefamily')]")))
        return dropbar_beekeeper

    def button_submit(self):
        button_submit = WebDriverWait(self.browser, 5).until(
            EC.element_to_be_clickable((By.XPATH,'//button[text()="Submit"]')))
        return button_submit

    def button_koszonom_nem(self):
        button_koszonom_nem = WebDriverWait(self.browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Köszönöm, nem']")))
        return button_koszonom_nem

    def text_wrong_input(self):
        try:
            elements = self.browser.find_elements(By.CLASS_NAME, "text-danger")
            return elements[1] if len(elements) > 1 else None
        except Exception:
            return None




