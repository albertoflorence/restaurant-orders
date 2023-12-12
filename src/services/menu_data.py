# Req 3
import csv

from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        with open(source_path) as csv_file:
            data = csv.DictReader(csv_file)
            self._dishes_table = {}
            self.dishes = set()
            self._process_data(data)

    def _get_dish(self, dish: Dish) -> Dish:
        return (
            self._dishes_table.get(dish)
            if dish in self._dishes_table
            else dish
        )

    def _add_dish(self, new_dish: Dish) -> Dish:
        dish = self._get_dish(new_dish)
        self.dishes.add(dish)
        self._dishes_table[dish] = dish
        return dish

    def _process_data(self, data: csv.DictReader) -> None:
        for row in data:
            dish = self._add_dish(Dish(row["dish"], float(row["price"])))
            dish.add_ingredient_dependency(
                Ingredient(row["ingredient"]), int(row["recipe_amount"])
            )
