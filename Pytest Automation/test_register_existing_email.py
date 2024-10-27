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

def test_reg_existing_user(browser):
    lgn_btn = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")
    lgn_btn.click()
    expected_text = "New User Signup!"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/h2").text
    assert expected_text == actual_text, f"Error while checking text on signup page: Text:{actual_text}"

    name = browser.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[2]")
    name.send_keys("Valerio")
    email = browser.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[3]")
    email.send_keys("avream@gmail.com")
    sign_btn = browser.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/button")
    sign_btn.click()
    time.sleep(5)
    expected_txt = "Email Address already exist!"
    actual_txt = browser.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/p").text
    assert expected_txt == actual_txt, f"Error while checking the error message: {actual_txt}"
