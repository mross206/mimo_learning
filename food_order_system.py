italian_food = ["Pasta Bolognese", "Pepperoni Pizza", "Margherita Pizza", "Lasagna"]

indian_food = ["Curry", "Chutney", "Samosa", "Naan"]

def find_meal(name, menu):
  if name in menu:
    return name
  else:
    return None

def select_meal(name, food_type):
  if food_type == "Italian":
    return find_meal(name, italian_food)
  elif food_type == "Indian":
    return find_meal(name, indian_food)
  else:
    return None

def display_available_meals(food_type):
  if food_type == "Italian":
    print("Available Italian Meals: ")
    for meals in italian_food:
      print(meals)
  elif food_type == "Indian":
    print("Available Indian Meals: ")
    for meals in indian_food:
      print(meals)
  else:
    print("Invalid food type")
  

def create_summary(name, amount, food_type):
  order = select_meal(name, food_type)
  if order:
    return f"You ordered {amount} {name}"
  else:
    return "Meal not found"

print("Welcome to the Food Order System!")

type_input = input("What type of food do you want?")

display_available_meals(type_input)

name_input = input("Enter the name of the meal you want to order: ")
amount_input = int(input("Enter the quantity you want to order: "))

result = create_summary(name_input, amount_input, type_input)
print(result)