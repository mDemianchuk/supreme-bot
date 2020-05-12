import util
from bot import Bot
from threading import Thread


def buy_item(item, billing_info):
    item_name = item["name"].strip()
    item_colorway_position = item["colorwayPosition"].strip()
    item_size = item["size"].strip()
    bot = Bot()
    bot.start()
    bot.select_item(item_name)
    if item_colorway_position:
        bot.select_colorway(item_colorway_position)
    if item_size:
        bot.select_size(item_size)
    bot.add_to_cart()
    bot.go_to_checkout()
    bot.fill_in_checkout_form(billing_info)
    bot.agree_with_terms()


def main():
    settings = util.get_settings()
    for item in settings["items"]:
        try:
            Thread(target=buy_item, args=(
                item, settings["billingInfo"])).start()
        except:
            print("Unable to start a task for the {}".format(item["name"]))


if __name__ == "__main__":
    main()
