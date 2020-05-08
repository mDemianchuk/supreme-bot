import time
from setup import *
from webdriver import WebDriver

START_URL = "https://www.supremenewyork.com/mobile#categories/new"


class Bot:
    def __init__(self):
        self.webdriver = WebDriver()

    def start(self):
        self.webdriver.open_url(START_URL)

    def quit(self):
        self.webdriver.quit()

    def is_item_selected(self):
        return self.webdriver.get_current_url() != START_URL

    def is_item_present(self, item_name):
        return bool(self.webdriver.find_element_by_visible_text(item_name))

    def select_item(self, item_name):
        while not self.is_item_selected:
            if self.is_item_present(item_name):
                self.select_item(item_name)
            else:
                self.webdriver.refresh()
        self.webdriver.find_element_by_visible_text(item_name).click()

    def select_colorway(self, colorway_position):
        colorway_box_x_path = '//*[@id="style-selector"]/li[{}]'.format(
            colorway_position
        )
        colorway_box = self.webdriver.find_element_by_x_path(colorway_box_x_path)
        colorway_box.click()

    def select_size(self, item_size):
        self.webdriver.select_dropdown_option('//*[@id="size-options"]', ITEM_SIZE)

    def add_to_cart(self):
        self.webdriver.find_element_by_visible_text("add to cart").click()

    def go_to_checkout(self):
        self.webdriver.find_element_by_visible_text("CHECK OUT").click()

    def fill_in_checkout_form(self):
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[1]/td/input', NAME
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[2]/td/input', EMAIL
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[3]/td/input', PHONE
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[4]/td/input', ADDRESS
        )
        if bool(UNIT):
            self.webdriver.fill_in_input_field(
                '//*[@id="billing-info"]/tbody/tr[5]/td/input', UNIT
            )
        self.webdriver.fill_in_input_field(
            '//*[@id="address_inputs_table"]/tbody/tr/td[1]/input', ZIP
        )
        # The class of this div is "needsclick", so we click on it just in case
        self.webdriver.find_element_by_x_path(
            '//*[@id="address_inputs_table"]/tbody/tr/td[3]/div/div[1]'
        ).click()
        self.webdriver.select_dropdown_option('//*[@id="order_billing_state"]', STATE)
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="credit card number"]', CC_NUMBER
        )
        self.webdriver.select_dropdown_option('//*[@id="credit_card_month"]', EXP_M)
        self.webdriver.select_dropdown_option('//*[@id="credit_card_year"]', EXP_Y)
        self.webdriver.fill_in_input_field('//input[@placeholder="cvv"]', CVV)
        self.webdriver.find_element_by_x_path('//*[@id="order_terms"]').click()


if __name__ == "__main__":
    bot = Bot()
    bot.start()
    start_time = time.time()
    bot.select_item(ITEM_NAME)
    bot.select_colorway(ITEM_COLORWAY_POSITION)
    bot.select_size(ITEM_SIZE)
    bot.add_to_cart()
    bot.go_to_checkout()
    bot.fill_in_checkout_form()
    bot.quit()
    print(time.time() - start_time)
