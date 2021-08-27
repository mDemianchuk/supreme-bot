import os

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from utils.logging_util import log_warning

ELEMENT_WAIT_TIME = 1


class WebDriver:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=self.__get_chromedriver_path(), options=self.__get_options()
        )

    @staticmethod
    def __get_chromedriver_path():
        current_dir_path = os.path.dirname(__file__)
        chromedriver_path = os.path.join(current_dir_path, "../chromedriver")
        # for Windows users
        if os.name == "nt":
            chromedriver_path += ".exe"
        return chromedriver_path

    @staticmethod
    def __get_options():
        options = webdriver.ChromeOptions()
        options.add_experimental_option("mobileEmulation", {"deviceName": "iPad"})
        options.add_experimental_option("detach", True)
        options.add_argument("--window-size=768,1024")
        return options

    def get_current_url(self):
        return self.driver.current_url

    def open_url(self, url: str):
        self.driver.get(url)

    def refresh(self):
        self.driver.refresh()

    def find_element_by_x_path(self, element_x_path: str):
        try:
            return WebDriverWait(self.driver, ELEMENT_WAIT_TIME).until(
                ec.visibility_of_element_located((By.XPATH, element_x_path))
            )
        except TimeoutException:
            log_warning(f"Element isn't located yet: {element_x_path}")

    def find_element_by_visible_text(self, element_text: str):
        case_insensitive_element_x_path = (
            "//*[text()[contains(translate(., '{}', '{}'), '{}')]]".format(
                element_text.upper(), element_text.lower(), element_text.lower()
            )
        )
        return self.find_element_by_x_path(case_insensitive_element_x_path)

    @staticmethod
    def click_on_element(element: WebElement or None):
        if element is None:
            log_warning("Unable to click - element is empty.")
            return False
        element.click()
        return True

    def select_dropdown_option(self, dropdown_x_path: str, option_text: str):
        option_x_path = "{}/option[text()='{}']".format(dropdown_x_path, option_text)
        option = self.find_element_by_x_path(option_x_path)
        return self.click_on_element(option)

    def fill_in_input_field(self, input_field_x_path: str, text: str):
        input_field = self.find_element_by_x_path(input_field_x_path)
        for character in text:
            input_field.send_keys(character)
        return True

    def quit(self):
        self.driver.quit()
