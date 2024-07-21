from selenium.webdriver.common.by import By
from datetime import datetime
import pytest
@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("arun.motoori@gmail.com")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        # driver.find_element(By.CLASS_NAME,"btn btn-primary").click()
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        assert self.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed()
        self.driver.quit()

    def test_login_with_invalid_mailid_valid_password(self):
        self.driver.find_element(By.XPATH,"//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT,"Login").click()
        self.driver.find_element(By.ID,"input-email").send_keys("generate_email_with_timestamp()")
        self.driver.find_element(By.ID,"input-password").send_keys("12345")
        # driver.find_element(By.CLASS_NAME,"btn btn-primary").click()
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(expected_warning_message)
        self.driver.quit()

    def test_login_with_valid_mailid_invalid_password(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "input-email").send_keys("arun.motoori@gmail.com")
        self.driver.find_element(By.ID, "input-password").send_keys("1234567")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message)
        self.driver.quit()

    def test_login_without_entering_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.XPATH, "//ul[@class='dropdown-menu dropdown-menu-right']//a[normalize-space()='Login']").click()
        self.driver.find_element(By.ID, "input-email").send_keys()
        self.driver.find_element(By.ID, "input-password").send_keys()
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[@id='account-login']/div[1]").text.__contains__(
            expected_warning_message)
        self.driver.quit()

    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
        return "amotoori"+time_stamp+"@gmail.com"

























