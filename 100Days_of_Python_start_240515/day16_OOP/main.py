# OOP를 사용해서 자동 커피 머신 만들기

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from mondy_machine import MoneyMachine

'''
어떻게 시작해야할까?

객체를 보며 객체의 내용을 분석할까?

내가 뭘 해야하는지를 좀 생각하고 시작할까?

해야할 일을 적고, 필요한 클래스를 정리해보자.

그리고 끝나면 반드시 강사님은 어떻게 해결했는지 확인하자.
'''

'''
남의 클래스를 사용할 때는, 그리고 설명서만 보고 사용할 때는,
각각의 메서드가 어떤 작용을 하는지 그냥 실행해보면서, 익혀.
그 다음에 코드를 짜기 시작하자.
'''


# menu에 report를 입력하면 보여주도록,
# MoneyMachin 클래스 report()


# 가장 먼저 할 것 메뉴아이템 만들기

# 이거 안해도 Menu 불러오면 __init__ 해놓네

# espresso = MenuItem("espresso",50,0,18,1.5)
# latte = MenuItem("latte",200,150,24,2.5)
# cappuccino = MenuItem("cappuccino",250,100,24,3.0)

# class define
menu = Menu() #  automatically menu created
coffeemaker = CoffeeMaker()
moneyMachine = MoneyMachine()

# print(menu.find_drink('latt'))
# print(menu.get_items())
#
# drink = input("drink: ")
# print(menu.find_drink(drink).name)


# 입력 받아야지.
while 1:
    drink = input(f'What do you want to drink? ({menu.get_items()}) ')

    if drink == 'off':
        break

    elif drink == 'report':
        coffeemaker.report()
        moneyMachine.report()
        print()
        continue

    drink = menu.find_drink(drink)
    # if drink is in menu
    if not drink == None:
        # check coffee sufficient
        if not coffeemaker.is_resource_sufficient(drink):
            continue
        # pay money
        if moneyMachine.make_payment(drink.cost) :
            coffeemaker.make_coffee(drink)
    print()


