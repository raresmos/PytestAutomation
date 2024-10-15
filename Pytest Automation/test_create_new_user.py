import pytest
import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

import time


def test_luch_browser(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")


def test_register_user(browser):
    log_in_button =WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")))
    log_in_button.click()
    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New User Signup!')]")))
    page_source = browser.page_source
    assert "New User Signup!" in page_source , "The text is not visible"
    name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.NAME,"name")))
    name.send_keys("Avram")
    email = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]")))
    email.send_keys("avream@gmail.com")
    signup_button = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div/div[3]/div/form/button")))
    signup_button.click()
    time.sleep(5)

def test_input_new_user(browser):
    page_source = None
    try:
        text = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "/html/body/section/div/div/div/div[1]/h2/b")))
        if text.text == "ENTER ACCOUNT INFORMATION":
            print("Test is visible")
    except Exception as e:
        print(f"Error: {e}")
    browser.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[1]/div[1]/label/div/span/input").click()
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/div[4]/input").send_keys('12345')
    Select(browser.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[1]/div/select")).select_by_visible_text("7")
    Select(browser.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[2]/div/select")).select_by_visible_text("January")
    Select(browser.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/div[5]/div/div[3]/div/select")).select_by_visible_text("1995")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[1]/input").send_keys("Rares")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[2]/input").send_keys("Mos")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[4]/input").send_keys("Placa Real")
    Select(browser.find_element(By.XPATH,"/html/body/section/div/div/div/div[1]/form/p[6]/select")).select_by_visible_text("Canada")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[7]/input").send_keys("Barcelona")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div/form/p[8]/input").send_keys("Barcelona")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[9]/input").send_keys("08020")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/p[10]/input").send_keys("5588899")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div[1]/form/button").click()
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'ACCOUNT CREATED!')]"))
        )
        page_source = browser.page_source
        assert "ACCOUNT CREATED!" in page_source, "The text is not visible"
    except Exception as e:
        print(f"Error while waiting for text: {e}")
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div/a").click()

    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(By.XPATH, "//*[contains(text(), 'Logged in as')]")
        )
        page_source = browser.page_source
        user_name_element = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a/b")
        user_name_text = user_name_element.text
        expected_username = "Avram"
        assert user_name_text == expected_username, f"Expected '{expected_username}', but got '{user_name_text}'"
    except Exception as e:
        print(f"Error while checking if you are logged in: {e}")



# def test_delete_account(browser):
#     browser.get("https://www.automationexercise.com/")
#     assert "Automation Exercise" in browser.title
#     try:
#
#         accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
#         accept_button.click()
#     except:
#         print("Pop-up is not visible")
#     log_in_button = WebDriverWait(browser, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[4]/a")))
#     log_in_button.click()
#     email_login = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[2]")
#     password_login = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/input[3]")
#     login_button = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/form/button")
#     delete_acc_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")))
#     try:
#         text_check = browser.find_element(By.XPATH, "/html/body/section/div/div/div[1]/div/h2")
#         if text_check.text == "Login to your account":
#             email_login.send_keys("avream@gmail.com")
#             password_login.send_keys("12345")
#             login_button.click()
#             delete_acc_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")))
#             delete_acc_btn.click()
#     except Exception as e:
#         print(f"Error while login: {e}")





