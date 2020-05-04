import time
import chromedriver_binary
from setup import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element_by_locator(locator):
    try:
        return WebDriverWait(driver, TIMEOUT_THRESHOLD).until(EC.visibility_of_element_located(locator))
    except TimeoutException:
        print("Item isn't found yet")

def find_element_by_visible_text(text):
    return find_element_by_locator((By.XPATH, "//*[contains(text(), '{}')]".format(text)))

def select_dropdown_option(dropdown_x_path, option_text):
    option_x_path = "{}/option[text()='{}']".format(dropdown_x_path, option_text)
    option = find_element_by_locator((By.XPATH, option_x_path))
    option.click()

def fill_in_input_field(input_field_x_path, text):
    input_field = find_element_by_locator((By.XPATH, input_field_x_path))
    if input_field:
        input_field.click()
        for character in text:
            input_field.send_keys(character)
            time.sleep(TYPING_DELAY)

def is_item_present(item_name):
    return bool(find_element_by_visible_text(item_name))

def select_item(item_name):
    find_element_by_visible_text(item_name).click()
    
def select_colorway(colorway_position):
    colorway_box_x_path = '//*[@id="style-selector"]/li[{}]'.format(colorway_position)
    colorway_box = find_element_by_locator((By.XPATH, colorway_box_x_path))
    colorway_box.click()

def select_size(item_size):
    select_dropdown_option('//*[@id="size-options"]', ITEM_SIZE)

def add_to_cart():
    find_element_by_visible_text('add to cart').click()

def go_to_checkout():
    find_element_by_visible_text('CHECK OUT').click()

def fill_in_checkout_form():
    fill_in_input_field('//*[@id="billing-info"]/tbody/tr[1]/td/input', NAME)
    fill_in_input_field('//*[@id="billing-info"]/tbody/tr[2]/td/input', EMAIL)
    fill_in_input_field('//*[@id="billing-info"]/tbody/tr[3]/td/input', PHONE)
    fill_in_input_field('//*[@id="billing-info"]/tbody/tr[4]/td/input', ADDRESS)
    if bool(UNIT):
        fill_in_input_field('//*[@id="billing-info"]/tbody/tr[5]/td/input', UNIT)
    fill_in_input_field('//*[@id="address_inputs_table"]/tbody/tr/td[1]/input', ZIP)
    # The class of this div is "needsclick", so we click on it just in case
    find_element_by_locator((By.XPATH, '//*[@id="address_inputs_table"]/tbody/tr/td[3]/div/div[1]')).click()
    select_dropdown_option('//*[@id="order_billing_state"]', STATE)
    fill_in_input_field('//input[@placeholder="credit card number"]', CC_NUMBER)
    select_dropdown_option('//*[@id="credit_card_month"]', EXP_M)
    select_dropdown_option('//*[@id="credit_card_year"]', EXP_Y)
    fill_in_input_field('//input[@placeholder="cvv"]', CVV)
    find_element_by_locator((By.XPATH, '//*[@id="order_terms"]')).click()

try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", { "deviceName": "iPad" })
    chrome_options.add_argument("--window-size=768,1024")
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(START_URL)
    while driver.current_url == START_URL:
        if is_item_present(ITEM_NAME):
            select_item(ITEM_NAME)
        else:
            driver.refresh()
    start_time = time.time()
    select_colorway(ITEM_COLORWAY_POSITION)
    select_size(ITEM_SIZE)
    add_to_cart()
    go_to_checkout()
    fill_in_checkout_form()
    print("--- %s seconds ---" % (time.time() - start_time))
finally:
    driver.quit()