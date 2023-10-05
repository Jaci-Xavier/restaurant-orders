import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.__parse_menu_data(source_path)

    def __parse_menu_data(self, source_path: str):
        dishes = {}

        with open(source_path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            for line in csv_reader:
                dish_name, price, ingredient_name, recipe_amount = (
                    line['dish'], float(line['price']), line['ingredient'],
                    int(line['recipe_amount'])
                )

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, price)

                dish = dishes[dish_name]
                dish.add_ingredient_dependency(
                    Ingredient(ingredient_name), recipe_amount
                )
        return set(dishes.values())
