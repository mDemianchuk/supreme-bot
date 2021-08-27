import time
from bot import Bot
from services.setting_loader import SettingLoader
from utils.logging_util import log_message


def main():
    items = SettingLoader.load_items()
    billing_info = SettingLoader.load_billing_info()

    bot = Bot("https://www.supremenewyork.com/mobile#categories/new")
    start_time = time.time()
    item_index = 0
    while item_index < len(items):
        item = items[item_index]

        bot.go_to_start_page()
        while bot.is_on_start_page():
            if not bot.select_item(item.name):
                bot.refresh()
        log_message(f"Item {item.name} selected.")

        if item.color and bot.select_color(item.color):
            log_message(f"Color {item.color} selected.")

        if bot.select_size(item.size):
            log_message(f"Size {item.size} selected.")

        if bot.add_to_cart():
            item_index += 1
            log_message(f"Item {item.name} successfully added to cart.")

    if bot.go_to_checkout():
        log_message("Proceeded to checkout successfully.")

    log_message("Filling in the checkout form.")
    bot.fill_in_checkout_form(billing_info)

    if bot.agree_to_terms():
        log_message("Agreed to terms.")

    # Uncomment this block of code to process the payment automatically
    #    if bot.process_payment():
    #        log_message("Payment is processing.")

    log_message(f"Total time: {time.time() - start_time}")


if __name__ == "__main__":
    main()
