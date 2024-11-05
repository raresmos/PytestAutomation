from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
import time



def test_subscription_cartPage(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    cart_btn = browser.find_element(By.CLASS_NAME, "fa.fa-shopping-cart")
    cart_btn.click()
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    expected_text = "SUBSCRIPTION"
    actual_text = browser.find_element(By.XPATH, "/html/body/footer/div[1]/div/div/div[2]/div/h2")
    assert  expected_text in actual_text.text, f"The expected text is not visible. The visible text is {actual_text}"
    email_input = browser.find_element(By.ID, "susbscribe_email")
    email_input.send_keys("avram21@gmail.com")
    send_btn = browser.find_element(By.ID, "subscribe")
    send_btn.click()
    expected_txt = "You have been successfully subscribed!"
    try:
        actual_txt = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'You have been successfully subscribed!')]")))
        assert expected_txt in actual_txt.text, f"The message is not displayed. Actual message is {actual_txt}"
    except:
        print('Message is not displayed')