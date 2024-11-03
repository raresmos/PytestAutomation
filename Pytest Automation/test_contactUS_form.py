from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time


def test_contact_form(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    contact_btn = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[8]/a")
    contact_btn.click()
    expected_text = "GET IN TOUCH"
    actual_text = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/h2")
    assert actual_text.is_displayed(), f"Expected text '{expected_text}' is not visible on the page"

    name_input = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[1]/input")
    name_input.send_keys("Avram")
    email_input = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[2]/input")
    email_input.send_keys("avram@gmail.com")
    subject_input = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[3]/input")
    subject_input.send_keys("Product")
    message_input = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[4]/textarea")
    message_input.send_keys("I would like to have more information about the products")
    import_btn = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[5]/input")
    file_path = "/Users/mos/Library/Mobile Documents/com~apple~CloudDocs/Rares Mos.pdf"
    import_btn.send_keys(file_path)
    submit_btn = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[3]/form/div[6]/input")
    submit_btn.click()
    time.sleep(5)

    try:
        alert = WebDriverWait(browser, 5).until(EC.alert_is_present())
        alert.accept()
        expected_text_success = "Success! Your details have been submitted successfully."
        actual_text_success = browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[2]").text
        assert expected_text_success == actual_text_success
    except TimeoutException:
        assert False, "The text is not displayed"







