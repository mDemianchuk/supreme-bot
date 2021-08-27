import util
import logging
from bot import Bot
import time


def main():
    logging.basicConfig(format="%(levelname)s: %(asctime)s - %(message)s",
                        datefmt="%I:%M:%S", level=logging.INFO)
    settings = util.get_settings()
    items = settings["items"]
    billing_info = settings["billingInfo"]

    bot = Bot("https://www.supremenewyork.com/mobile#categories/Jackets")
    logging.info("Initialized a bot instance")
    start_time = time.time()
    item_index = 0
    while item_index != len(items):
        item_name = items[item_index]["name"].strip()
        item_color = items[item_index]["color"].strip()
        item_size = items[item_index]["size"].strip()

        bot.go_to_start_page()
        while bot.is_on_start_page():
            if not bot.select_item(item_name):
                bot.refresh()
        logging.info("Item {} selected".format(item_name))

        if item_color and bot.select_color(item_color):
            logging.info("Colorway at position {} selected".format(
                item_color))

        if item_size and bot.select_size(item_size):
            logging.info("Size {} selected".format(item_size))

        if bot.add_to_cart():
            item_index += 1
            logging.info(
                "Item {} successfully added to cart".format(item_name))

    if bot.go_to_checkout():
        logging.info("Proceeded to checkout successfully")

    logging.info("Filling in the checkout form")
    bot.fill_in_checkout_form(billing_info)

    if bot.agree_to_terms():
        logging.info("Agreed to temrs")

    logging.info(f"Total time: {time.time() - start_time}")


# Uncomment this block of code to process the payment automatically
#    if bot.process_payment():
#        logging.info("Payment is processing")


if __name__ == "__main__":
    main()
