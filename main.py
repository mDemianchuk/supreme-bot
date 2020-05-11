import time
import util
from bot import Bot


if __name__ == "__main__":
    bot = Bot(util.get_settings())
    bot.start()
    start_time = time.time()
    bot.select_item()
    bot.select_colorway()
    bot.select_size()
    bot.add_to_cart()
    bot.go_to_checkout()
    bot.fill_in_checkout_form()
    bot.agree_with_terms()
    print(time.time() - start_time)
