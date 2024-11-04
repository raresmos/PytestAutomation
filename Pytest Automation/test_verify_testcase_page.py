from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time




def test_case_page(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    case_btn = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")
    case_btn.click()
    expected_text = "TEST CASES"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div[1]/div/h2/b").text
    assert expected_text in actual_text, f"You are not on the test cases page. Actual page: {actual_text}"