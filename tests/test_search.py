from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_for_a_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME,"search").send_keys("HP")
    driver.find_element(By.XPATH,"//button[contains(@class,'btn-default')]").click()

    # Wait for the product link to be visible
    WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "HP LP3065"))
    )
    assert driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()

    driver.quit()


def test_search_for_an_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME,"search").send_keys("Honda")
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()

def test_search_without_entering_any_product_name():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.NAME, "search").send_keys()
    driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
    expected_text = "There is no product that matches the search criteria."
    assert driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
    driver.quit()








