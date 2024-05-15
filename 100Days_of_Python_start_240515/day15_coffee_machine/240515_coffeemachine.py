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

units = {
    "water": 'ml',
    "milk": 'ml',
    "coffee": 'g',
}

coins = {
    "quarters" : .25,
    "dimes" : .1 ,
    "nickels" : .05,
    "pennies" : .01
}

# TODO : 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”

def asking():

    menu = input("What would you like ? (espresso/latte/cappuccino) ")

    return menu


# TODO : 3. Print report

def print_report():
    for src_key in resources.keys():
        print(f'{src_key}: {resources[src_key]}{units[src_key]}')
    print(f'Money: ${profit}\n')

# TODO : 4. Check resources sufficient?
def is_sufficient_resources(drink):
    # 메뉴에서 필요한 재료를 추출
    for ingredient in MENU[drink]["ingredients"].keys():
        if resources[ingredient] < MENU[drink]["ingredients"][ingredient]:
            print(f'Sorry there is not enough {ingredient}')
            return False
    return True

# TODO : 5. Process coins

def Incert_coins():
    total_cost = 0
    for (coin, value) in coins.items():
        cost = value * int(input(f'How many {coin}? '))
        total_cost += cost
    print(f'total : {total_cost}')
    return total_cost


# TODO : 6. Check transaction successful?
def is_suficient_cost(drink):
    input_cost = Incert_coins()
    require_cost = MENU[drink]["cost"]
    print(f"{drink}'s price is {require_cost}")
    change = input_cost - require_cost
    if change < 0:
        print("Sorry that's not enough money, Money refunded.")
        return False
    # 돈이 충분하면
    print(f"Here is ${change:.2f} in change.")
    print(f'Here is your {drink} ☕️ Enjoy!\n')
    return True

# TODO : 7. Make Coffee

def process_resources(drink):
    global profit

    for ingredient in MENU[drink]["ingredients"].keys():
        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
    profit += MENU[drink]["cost"]

# TODO : 2. Turn off the Coffee Machine by entering “off” to the prompt.

if __name__ == "__main__" :
    print(MENU.keys())
    while 1:
        menu = asking()
        if menu == 'off':
            break
        elif menu == 'report':
            print_report()
        elif menu in MENU.keys():
            # 자원 부족하면 처음으로
            if not is_sufficient_resources(menu):
                continue
            # 자원이 충분하면
            # 돈이 충분한지
            if is_suficient_cost(menu):
                process_resources(menu)


