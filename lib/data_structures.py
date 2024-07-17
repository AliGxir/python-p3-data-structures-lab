spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    name_list = []
    for food in spicy_foods:
        name_list.append(food.get("name"))
    return name_list

def get_spiciest_foods(spicy_foods):   
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level = food["heat_level"] * "🌶"
        # use different quotations to distinguish print from keys
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level}")

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if cuisine is food["cuisine"]:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food["heat_level"] for food in spicy_foods)
    average_heat = total_heat_level / len(spicy_foods)
    return int(average_heat)

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods.copy()
    new_list.append(spicy_food)
    return new_list 
# can't just use append => None, so copy to a new list, then append to it and can be returned