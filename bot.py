from webdriver import WebDriver
from utils.logging_util import log_message
from models.billing_info import BillingInfo


class Bot:
    def __init__(self, start_page_url: str):
        self.webdriver = WebDriver()
        self.start_page_url = start_page_url
        log_message("Initialized a bot instance.")

    def go_to_start_page(self):
        self.webdriver.open_url(self.start_page_url)

    def refresh(self):
        self.webdriver.refresh()

    def quit(self):
        self.webdriver.quit()

    def is_on_start_page(self):
        return self.webdriver.get_current_url() == self.start_page_url

    def select_item(self, item_name: str):
        item = self.webdriver.find_element_by_visible_text(item_name)
        return self.webdriver.click_on_element(item)

    def select_color(self, item_color: str):
        color_box_x_path = '//*[@id="styles"]/ul/li[{}]'.format(
            item_color)
        color_box = self.webdriver.find_element_by_x_path(
            color_box_x_path)
        return self.webdriver.click_on_element(color_box)

    def select_size(self, item_size: str):
        return self.webdriver.select_dropdown_option('//*[@id="size-options"]', item_size)

    def add_to_cart(self):
        add_to_cart_button = self.webdriver.find_element_by_visible_text(
            "add to cart")
        return self.webdriver.click_on_element(add_to_cart_button)

    def go_to_checkout(self):
        checkout_button = self.webdriver.find_element_by_visible_text(
            "check out")
        return self.webdriver.click_on_element(checkout_button)

    def fill_in_checkout_form(self, billing_info: BillingInfo):
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[1]/td/input', billing_info.full_name
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[2]/td/input', billing_info.email
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[3]/td/input', billing_info.phone
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[4]/td/input', billing_info.address
        )
        if billing_info.unit:
            self.webdriver.fill_in_input_field(
                '//*[@id="billing-info"]/tbody/tr[5]/td/input', billing_info.unit
            )
        self.webdriver.fill_in_input_field(
            '//*[@id="address_inputs_table"]/tbody/tr/td[1]/input', billing_info.zip_code
        )
        self.webdriver.select_dropdown_option(
            '//*[@id="order_billing_state"]', billing_info.state)
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="credit card number"]', billing_info.cc_number
        )
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_month"]', billing_info.exp_month)
        self.webdriver.select_dropdown_option(
            '//*[@id="credit_card_year"]', billing_info.exp_year)
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="cvv"]', billing_info.cvv)

    def agree_to_terms(self):
        terms_checkbox = self.webdriver.find_element_by_x_path(
            '//*[@id="order_terms"]')
        return self.webdriver.click_on_element(terms_checkbox)

    def process_payment(self):
        process_payment_button = self.webdriver.find_element_by_visible_text(
            "process payment")
        return self.webdriver.click_on_element(process_payment_button)
