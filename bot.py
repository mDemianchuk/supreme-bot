from webdriver import WebDriver

START_URL = "https://www.supremenewyork.com/mobile#categories/new"


class Bot:
    def __init__(self, settings):
        self.webdriver = WebDriver()
        self.settings = settings

    def start(self):
        self.webdriver.open_url(START_URL)

    def quit(self):
        self.webdriver.quit()

    def is_item_selected(self):
        return self.webdriver.get_current_url() != START_URL

    def is_item_present(self):
        return bool(self.webdriver.find_element_by_visible_text(self.settings["itemName"]))

    def select_item(self):
        item_name = self.settings["itemName"]
        while not self.is_item_selected:
            if self.is_item_present(item_name):
                self.select_item(item_name)
            else:
                self.webdriver.refresh()
        self.webdriver.find_element_by_visible_text(item_name).click()

    def select_colorway(self):
        colorway_box_x_path = '//*[@id="style-selector"]/li[{}]'.format(
            self.settings["itemColorwayPosition"]
        )
        colorway_box = self.webdriver.find_element_by_x_path(colorway_box_x_path)
        colorway_box.click()

    def select_size(self):
        self.webdriver.select_dropdown_option('//*[@id="size-options"]', self.settings["itemSize"])

    def add_to_cart(self):
        self.webdriver.find_element_by_visible_text("add to cart").click()

    def go_to_checkout(self):
        self.webdriver.find_element_by_visible_text("CHECK OUT").click()

    def fill_in_checkout_form(self):
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[1]/td/input', self.settings["fullName"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[2]/td/input', self.settings["email"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[3]/td/input', self.settings["phone"]
        )
        self.webdriver.fill_in_input_field(
            '//*[@id="billing-info"]/tbody/tr[4]/td/input', self.settings["address"]
        )
        if bool(self.settings["unit"]):
            self.webdriver.fill_in_input_field(
                '//*[@id="billing-info"]/tbody/tr[5]/td/input', self.settings["unit"]
            )
        self.webdriver.fill_in_input_field(
            '//*[@id="address_inputs_table"]/tbody/tr/td[1]/input', self.settings["zip"]
        )
        # The class of this div is "needsclick", so we click on it just in case
        self.webdriver.find_element_by_x_path(
            '//*[@id="address_inputs_table"]/tbody/tr/td[3]/div/div[1]'
        ).click()
        self.webdriver.select_dropdown_option('//*[@id="order_billing_state"]', self.settings["state"])
        self.webdriver.fill_in_input_field(
            '//input[@placeholder="credit card number"]', self.settings["ccNumber"]
        )
        self.webdriver.select_dropdown_option('//*[@id="credit_card_month"]', self.settings["expM"])
        self.webdriver.select_dropdown_option('//*[@id="credit_card_year"]', self.settings["expY"])
        self.webdriver.fill_in_input_field('//input[@placeholder="cvv"]', self.settings["cvv"])
        self.webdriver.find_element_by_x_path('//*[@id="order_terms"]').click()