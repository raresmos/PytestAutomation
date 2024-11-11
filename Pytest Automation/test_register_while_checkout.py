import time
import selenium.webdriver.support.ui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, MoveTargetOutOfBoundsException
from selenium.webdriver.common.action_chains import ActionChains

def test_register_in_checkout(browser):
    browser.get("https://www.automationexercise.com/")
    assert "Automation Exercise" in browser.title
    try:

        accept_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[2]/div[1]/div[2]/div[2]/button[1]/p")))
        accept_button.click()
    except:
        print("Pop-up is not visible")

    # Add product in cart
    product_hover = browser.find_element(By.XPATH,
                                         "/html/body/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[1]/img")
    browser.execute_script("arguments[0].scrollIntoView(true);", product_hover)
    action = ActionChains(browser)
    action.move_to_element(product_hover).perform()
    add_cart = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/section[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div/div[1]/div[2]/div/a")))
    add_cart.click()

    view_cart_btn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/p[2]/a/u")))
    view_cart_btn.click()
    cart_page_text_expected = "Shopping Cart"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div[1]/ol/li[2]")
    assert cart_page_text_expected in actual_text.text, f"Error while checking cart page. Actual Text: {actual_text}"

    # Proceed to checkout
    browser.find_element(By.CLASS_NAME, "btn.btn-default.check_out").click()

    # Register/ Login
    browser.find_element(By.XPATH, "/html/body/section/div/section/div[2]/div/div/div[2]/p[2]/a/u").click()

    #Creating new user

    WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'New User Signup!')]")))
    page_source = browser.page_source
    assert "New User Signup!" in page_source , "The text is not visible"
    name = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[2]")))
    name.send_keys("Avram")
    email = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div/div[3]/div/form/input[3]")))
    email.send_keys("avream@gmail.com")
    signup_button = WebDriverWait(browser,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/section/div/div/div[3]/div/form/button")))
    signup_button.click()
    time.sleep(5)

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
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Logged in as')]")
        ))
        page_source = browser.page_source
        user_name_element = browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[10]/a/b")
        user_name_text = user_name_element.text
        expected_username = "Avram"
        assert user_name_text == expected_username, f"Expected '{expected_username}', but got '{user_name_text}'"
    except Exception as e:
        print(f"Error while checking if you are logged in: {e}")

    #Cart Button
    browser.find_element(By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[3]/a").click()

    #proceed to checkout
    browser.find_element(By.XPATH, "/html/body/section/div/section/div[1]/div/div/a").click()

    # Checking the adress and review order
    expected_text1 = "Address Details"
    expected_text2 = "Review Your Order"
    cart_details = browser.find_element(By.XPATH, "/html/body/section")
    assert expected_text1 and expected_text2 in cart_details.text, "Error while checking the expected text"

    # Input description in comms
    browser.find_element(By.CLASS_NAME, "form-control").send_keys("I like the products")

    #Place order
    browser.find_element(By.XPATH, "/html/body/section/div/div[7]/a").click()

    #Checkig the payment page
    payment_text = browser.find_element(By.XPATH, "/html/body/section/div/div[2]/h2")
    expected_payment_text = "Payment"
    assert expected_payment_text in payment_text.text, "Error while checking the payment page"

    #Insert payment details
    name = browser.find_element(By.NAME, "name_on_card")
    name.send_keys("Avram Micul")
    card_number = browser.find_element(By.CLASS_NAME, "form-control.card-number")
    card_number.send_keys("5555888899997777")
    cvc = browser.find_element(By.CLASS_NAME, "form-control.card-cvc")
    cvc.send_keys("311")
    month_expiration = browser.find_element(By.CLASS_NAME, "form-control.card-expiry-month")
    month_expiration.send_keys("02")
    year_expiration = browser.find_element(By.CLASS_NAME, "form-control.card-expiry-year")
    year_expiration.send_keys("2030")
    pay_order = browser.find_element(By.CLASS_NAME, "form-control.btn.btn-primary.submit-button")
    pay_order.click()

    #Checking te message for order placed.
    expected_order_text = "Congratulations! Your order has been confirmed!"
    actual_order_text = browser.find_element(By.XPATH, "/html/body")
    assert  expected_order_text in actual_order_text.text, "Error while checking the order text"

    #Continue to delete the account
    browser.find_element(By.XPATH, "/html/body/section/div/div/div/div/a").click()
    delete_acc_btn = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/header/div/div/div/div[2]/div/ul/li[5]/a")))
    delete_acc_btn.click()
    deleted_text = "ACCOUNT DELETED!"
    actual_text = browser.find_element(By.XPATH, "/html/body/section/div/div/div/h2/b").text
    assert deleted_text == actual_text, f"Error while checking deleted text: {actual_text}"









