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
    return [item['name'] for item in spicy_foods]


def get_spiciest_foods(spicy_foods): #returns a list of dicts where heat > 5
    return [item for item in spicy_foods if item['heat_level'] > 5]

def print_spicy_foods(spicy_foods): # Buffalo Wings (American) | Heat Level: 🌶🌶🌶
    for items in [ f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶'*item['heat_level']}" for item in spicy_foods ]:
        print(items)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    for items in [ f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶'*item['heat_level']}" for item in spicy_foods if item['heat_level'] > 5]:
        print(items)

def get_average_heat_level(spicy_foods):
    avg = 0
    for num in [item['heat_level'] for item in spicy_foods]:
        avg += num
    return avg / len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
