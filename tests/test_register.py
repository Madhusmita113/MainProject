from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By


def generate_email_with_timestamp():
    time_stamp = datetime.now().strftime("%y_%m_%d_%H_%M_%S")
    return "madhu" + time_stamp + "@gmail.com"


def test_register_valid_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("madhu")
    driver.find_element(By.ID,"input-lastname").send_keys("biswal")
    generated_email = generate_email_with_timestamp()
    driver.find_element(By.ID,"input-email").send_keys(generated_email)
    driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
    driver.find_element(By.ID,"input-password").send_keys("12345")
    driver.find_element(By.ID,"input-confirm").send_keys("12345")
    driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    driver.find_element(By.NAME,"agree").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_heading_text = "Your Account Has Been Created!"
    assert driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_heading_text)
    print("Generated_email:", generated_email)
    driver.quit()



def test_register_with_already_registered_mailid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH,"//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT,"Register").click()
    driver.find_element(By.ID,"input-firstname").send_keys("madhu")
    driver.find_element(By.ID,"input-lastname").send_keys("biswal")
    driver.find_element(By.ID,"input-email").send_keys("arun.motoori@gmail.com")
    driver.find_element(By.ID,"input-telephone").send_keys("1234567890")
    driver.find_element(By.ID,"input-password").send_keys("12345")
    driver.find_element(By.ID,"input-confirm").send_keys("12345")
    driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()
    driver.find_element(By.NAME,"agree").click()
    driver.find_element(By.XPATH,"//input[@value='Continue']").click()
    expected_warning_text = "Warning: E-Mail Address is already registered!"
    assert driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]").text.__eq__(expected_warning_text)
    driver.quit()


def test_register_with_no_credentials():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    driver.find_element(By.LINK_TEXT, "Register").click()
    driver.find_element(By.ID, "input-firstname").send_keys()
    driver.find_element(By.ID, "input-lastname").send_keys()
    driver.find_element(By.ID, "input-email").send_keys()
    driver.find_element(By.ID, "input-telephone").send_keys()
    driver.find_element(By.ID, "input-password").send_keys()
    driver.find_element(By.ID, "input-confirm").send_keys()
    driver.find_element(By.XPATH, "//input[@name='newsletter'][@value='1']").click()
    driver.find_element(By.NAME, "agree").click()
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    expected_warning_text = "If you already have an account with us, please login at the login page."
    assert driver.find_element(By.XPATH, "//div[@id='content']/child::p").text.__eq__(expected_warning_text)

    expected_warning_first_name ="First Name must be between 1 and 32 characters!"
    assert  driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div").text.__eq__(expected_warning_first_name)

    expected_warning_last_name="Last Name must be between 1 and 32 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div").text.__eq__(
        expected_warning_last_name)

    expected_warning_email = "E-Mail Address does not appear to be valid!"
    assert driver.find_element(By.XPATH,"//input[@id='input-email']/following-sibling::div").text.__eq__(
        expected_warning_email)

    expected_warning_telephone_no = "Telephone must be between 3 and 32 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div").text.__eq__(
        expected_warning_telephone_no)

    expected_warning_password = "password must be between 4 and 20 characters!"
    assert driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div").text.__eq__(
        expected_warning_password)
    driver.quit()









