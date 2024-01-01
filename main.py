MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_payment():
    print("Please insert the coins:")
    quarters = input("quarters:\n")
    dimes = input("dimes:\n")
    nickles = input("nickels:\n")
    pennies = input("pennies:\n:")
    summ = 0.25 * float(quarters) + 0.1 * float(dimes) + 0.05 * float(nickles) + 0.01 * float(pennies)
    return summ


def transaction_successful(cost,money):
    if money >= cost:
        change = round(money-cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(coffee_type , order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee_type} ☕️. Enjoy!")


is_on = True


while is_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_type == "off":
        is_on = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[coffee_type]
        if resource_sufficient(drink["ingredients"]):
            Money = process_payment()
            if transaction_successful(drink["cost"], Money):
                make_coffee(coffee_type,drink["ingredients"])

