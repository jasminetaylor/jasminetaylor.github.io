import random 
adjectives = ["Fresh ","Wild ","Crunchy ", "Spicy ", "Creamy ", "Cheesy ", "Sweet ", "Seasoned ", "Rich ", "Soft "]
cooking_styles = ["Seared ", "Roasted ", "Grilled ", "Steamed ", "Baked ", "Fried ", "Sautéd ", "Cured ", "Smoked ", "Braised " ]
list_of_foods = ["Fish", "Pasta", "Chicken", "Tacos", "Lobster", "Steak", "Lamb", "Biscuits", "Waffles", "Wraps"]

for i in range(10):
	random_adject = random.randint(0,len(adjectives)-1)
	random_style = random.randint(0,len(cooking_styles)-1)
	random_food = random.randint(0,len(list_of_foods)-1)
	menu = adjectives[random_adject] + cooking_styles[random_style] + list_of_foods[random_food]
	print(i)
	print(menu)