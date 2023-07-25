from menu_coffee_machine import MENU
from menu_coffee_machine import resources

missing_resource = False
money = 0
coins = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25
}


def check(resources, drink):
    global missing_resource
    global money
    if resources["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there's not enough water...")
        missing_resource = True
    else:
        missing_resource = False
    if drink != "espresso":
        if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there's not enough milk...")
            missing_resource = True
        else:
            missing_resource = False
    if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee...")
        missing_resource = True
    else:
        missing_resource = False


keep_working = True
while keep_working:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "report":
        print(f"""Water: {resources['water']}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money}""")
    elif drink == "turn off":
        print("Turning off...")
        missing_resource = True
        keep_working = False
    else:
        check(resources, drink)

    if not missing_resource and drink != "report" and drink != "turn off":
        coin_penny = int(input("How many pennies? "))
        coin_nickle = int(input("How many nickles? "))
        coin_dime = int(input("How many dimes? "))
        coin_quarter = int(input("How many quarters? "))
        payment = (coin_penny * coins["pennies"]) + (coin_nickle * coins["nickles"]) + (coin_dime * coins["dimes"]) + \
                  (coin_quarter * coins["quarters"])
        if payment >= MENU[drink]["cost"]:
            resources["coffee"] = resources["coffee"] - MENU[drink]["ingredients"]["coffee"]
            resources["water"] = resources["water"] - MENU[drink]["ingredients"]["water"]
            if drink != "espresso":
                resources["milk"] = resources["milk"] - MENU[drink]["ingredients"]["milk"]
            print(f"Here's your change: ${round(payment - MENU[drink]['cost'], 2)}")
            print(f"Here's your {drink}. Enjoy! ")
            money = money + MENU[drink]['cost']
        else:
            print("Sorry, that´s not enough money. Money refunded...")
