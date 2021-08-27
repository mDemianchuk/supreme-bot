from utils.json_util import read_json_file
from models.item import Item
from models.billing_info import BillingInfo


class SettingLoader:
    __settings_json = read_json_file("settings.json")

    @classmethod
    def load_items(cls):
        items = []
        for item_json in cls.__settings_json["items"]:
            item = Item(
                item_json["name"],
                item_json["color"],
                item_json["size"]
            )
            items.append(item)
        return items

    @classmethod
    def load_billing_info(cls):
        return BillingInfo(
            cls.__settings_json["billingInfo"]["fullName"],
            cls.__settings_json["billingInfo"]["email"],
            cls.__settings_json["billingInfo"]["phone"],
            cls.__settings_json["billingInfo"]["address"],
            cls.__settings_json["billingInfo"]["unit"],
            cls.__settings_json["billingInfo"]["zip"],
            cls.__settings_json["billingInfo"]["state"],
            cls.__settings_json["billingInfo"]["ccNumber"],
            cls.__settings_json["billingInfo"]["expM"],
            cls.__settings_json["billingInfo"]["expY"],
            cls.__settings_json["billingInfo"]["cvv"]
        )
