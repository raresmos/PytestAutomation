import pytest
import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_delete_account(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")
    log_in_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")))
    log_in_button.click()
    email_login = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
    password_login = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
    login_button = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button")
    delete_acc_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")))
    try:
        text_check = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2")
        if text_check.text == "Login to your account":
            email_login.send_keys("avream@gmail.com")
            password_login.send_keys("12345")
            login_button.click()
            delete_acc_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")))
            delete_acc_btn.click()
            deleted_msg = WebDriverWait(browser,10).until(EC.presence_of_element_located(By.XPATH, "//*[contains(text(), 'ACCOUNT DELETED!')]"))
            page_source = browser.page_source
            assert "ACCOUNT DELETED!" in page_source, "The account was not deleted. Test Failed"

    except Exception as e:
        print(f"Error while login: {e}")
        assert False, "Test failed due to an error"








