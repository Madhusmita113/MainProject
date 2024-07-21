from datetime import datetime
from selenium.webdriver.common.by import By
import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        return "madhu" + time_stamp + "@gmail.com"


    def test_register_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("madhu")
        self.driver.find_element(By.ID,"input-lastname").send_keys("biswal")
        self.driver.find_element(By.ID,"input-email").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_heading_text)
        self.driver.quit()

    def test_register_with_already_registered_mailid(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Register").click()
        self.driver.find_element(By.ID,"input-firstname").send_keys("madhu")
        self.driver.find_element(By.ID,"input-lastname").send_keys("biswal")
        self.driver.find_element(By.ID,"input-email").send_keys("arun.motoori@gmail.com")
        self.driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        self.driver.find_element(By.ID,"input-confirm").send_keys("12345")
        self.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME,"agree").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        expected_warning_text = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text.__eq__(expected_warning_text)
        self.driver.quit()

    def test_register_with_no_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.ID, "input-firstname").send_keys()
        self.driver.find_element(By.ID, "input-lastname").send_keys()
        self.driver.find_element(By.ID, "input-email").send_keys()
        self.driver.find_element(By.ID, "input-telephone").send_keys()
        self.driver.find_element(By.ID, "input-password").send_keys()
        self.driver.find_element(By.ID, "input-confirm").send_keys()
        self.driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_warning_text = "If you already have an account with us, please login at the login page."
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/child::p").text.__eq__(expected_warning_text)

        expected_warning_first_name = "First Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_warning_first_name)

        expected_warning_last_name="Last Name must be between 1 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
            expected_warning_last_name)

        expected_warning_email = "E-Mail Address does not appear to be valid!"
        assert self.driver.find_element(By.XPATH,"//input[@id='input-email']/following-sibling::div").text.__eq__(
            expected_warning_email)

        expected_warning_telephone_no = "Telephone must be between 3 and 32 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
            expected_warning_telephone_no)

        expected_warning_password = "password must be between 4 and 20 characters!"
        assert self.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
            expected_warning_password)
        self.driver.quit()









