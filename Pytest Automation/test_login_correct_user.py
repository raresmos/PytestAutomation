import time

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

def test_login(browser):
    browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a").click()
    expected_text = "Login to your account"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2").text
    assert expected_text == actual_text, f"Error while checking the login page: error {actual_text}"

    email = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
    email.send_keys("avream@gmail.com")
    password = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
    password.send_keys("12345")
    login_btn = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    time.sleep(5)
    login_btn.click()

    expected_txt = "Logged in as Avram"
    actual_txt = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a").text
    assert expected_txt == actual_txt, f"Error while checking user name: error {actual_text}"

