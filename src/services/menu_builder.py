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
        dishes = self._filter_dishes_with_ingredients(self.menu_data.dishes)
        menu = (
            self._menu_restrictions(dishes, restriction)
            if restriction
            else dishes
        )
        return self._format_menu_data(menu)

    def _filter_dishes_with_ingredients(self, dishes) -> set:
        return {
            dish
            for dish in dishes
            if self.inventory.check_recipe_availability(dish.recipe)
        }

    def _menu_restrictions(self, dishes, restriction) -> set:
        return {
            dish
            for dish in dishes
            if restriction not in dish.get_restrictions()
        }

    def _format_menu_data(self, dishes) -> Dict:
        return [
            {
                "dish_name": dish.name,
                "ingredients": dish.get_ingredients(),
                "price": dish.price,
                "restrictions": dish.get_restrictions(),
            }
            for dish in dishes
        ]
