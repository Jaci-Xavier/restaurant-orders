from typing import Dict, List

from services.inventory_control import InventoryMapping
from services.menu_data import MenuData

DATA_PATH = "data/menu_base_data.csv"
INVENTORY_PATH = "data/inventory_base_data.csv"


class MenuBuilder:
    def __init__(self, data_path=DATA_PATH, inventory_path=INVENTORY_PATH):
        self.menu_data = MenuData(data_path)
        self.inventory = InventoryMapping(inventory_path)

    def make_order(self, dish_name: str) -> None:
        try:
            curr_dish = [
                dish
                for dish in self.menu_data.dishes
                if dish.name == dish_name
            ][0]
        except IndexError:
            raise ValueError("Dish does not exist")

        self.inventory.consume_recipe(curr_dish.recipe)

    # Req 4
    def get_main_menu(self, restriction=None) -> List[Dict]:
        return list(map(lambda dish: {
            'dish_name': dish.name,
            'ingredients': dish.get_ingredients(),
            'price': dish.price,
            'restrictions': dish.get_restrictions()
         }, filter(lambda dish: restriction not in dish.get_restrictions()
                   and all(ingredient in self.inventory.inventory
                           for ingredient in dish
                           .get_ingredients()), self.menu_data.dishes)))
        # return [
        #     {
        #         'dish_name': dish.name,
        #         'ingredients': dish.get_ingredients(),
        #         'price': dish.price,
        #         'restrictions': dish.get_restrictions()
        #     }
        #     for dish in self.menu_data.dishes
        #     if (restriction not in dish.get_restrictions() and
        #         all(ingredient in self.inventory.inventory 
        #             for ingredient in dish.get_ingredients()))
        # ]
        # menu = []
        # for dish in self.menu_data.dishes:
        #     if restriction in dish.get_restrictions():
        #         continue

        #     available = all(
        #         ingredient in self.inventory.inventory
        #         for ingredient in dish.get_ingredients()
        #     )

        #     if available:
        #         dish_data = {
        #             'dish_name': dish.name,
        #             'ingredients': dish.get_ingredients(),
        #             'price': dish.price,
        #             'restrictions': dish.get_restrictions()
        #         }
        #         menu.append(dish_data)
        # return menu
