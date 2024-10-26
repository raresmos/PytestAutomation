import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_luch_browser(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

def test_login_wrongemail(browser):
    login_bnc = browser.find_element(By.CLASS_NAME, "fa.fa-lock")
    login_bnc.click()
    expected_text = "Login to your account"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2").text
    assert expected_text == actual_text, "Error while checking the expected text for login"
    email = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
    email.send_keys("birsu@gmail.com")
    password = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
    password.send_keys("12354")
    login = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    login.click()
    expected_txt = "Your email or password is incorrect!"
    actual_txt = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/p").text
    assert expected_txt == actual_txt, f"Error while checking the error message. Error msg: {actual_txt}"

