from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    order = input(f'What would you like? ({options})\n')
    if order != 'espresso' and order != 'latte' and order != 'cappuccino' and order != 'report' and order != 'off' :
        print('Invalid input')
        
    elif order == 'off':
        is_on = False
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)