import time
import util
from bot import Bot


if __name__ == "__main__":
    settings = util.get_settings()
    item_name = settings["itemInfo"]["name"].strip()
    item_colorway_position = settings["itemInfo"]["colorwayPosition"].strip()
    item_size = settings["itemInfo"]["size"].strip()
    billing_info = settings["billingInfo"]

    bot = Bot()
    bot.start()
    start_time = time.time()
    bot.select_item(item_name)
    if item_colorway_position:
        bot.select_colorway(item_colorway_position)
    if item_size:
        bot.select_size(item_size)
    bot.add_to_cart()
    bot.go_to_checkout()
    bot.fill_in_checkout_form(billing_info)
    bot.agree_with_terms()
    print(time.time() - start_time)
