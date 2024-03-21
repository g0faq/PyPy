class FoodInfo:
    def __init__(self, p, f, c):
        self.proteins = p
        self.fats = f
        self.carb = c

    def _add_(self, other):
        return FoodInfo(self.proteins + other.proteins,
                        self.fats + other.fats,
                        self.carb + other.carb)


food1 = FoodInfo(100, 100, 100)
food2 = FoodInfo(50, 60, 70)
food3 = food1 + food2
print(food1.get_proteins(), food1.get_fats(),
      food1.get_carbohydrates(), food1.get_kcalories())
print(food2.get_proteins(), food2.get_fats(),
      food2.get_carbohydrates(), food2.get_kcalories())
print(food3.get_proteins(), food3.get_fats(),
      food3.get_carbohydrates(), food3.get_kcalories())