import util
from bot import Bot
import time


def main():
    settings = util.get_settings()
    items = settings["items"]
    billing_info = settings["billingInfo"]

    bot = Bot()
    item_index = 0
    while item_index != len(items):
        item_name = items[item_index]["name"].strip()
        item_colorway_position = items[item_index]["colorwayPosition"].strip()
        item_size = items[item_index]["size"].strip()

        bot.go_to_start_page()
        bot.select_item(item_name)
        if item_colorway_position:
            bot.select_colorway(item_colorway_position)
        if item_size:
            bot.select_size(item_size)
        if bot.add_to_cart():
            item_index += 1

    bot.go_to_checkout()
    bot.fill_in_checkout_form(billing_info)
    bot.agree_with_terms()


if __name__ == "__main__":
    main()
