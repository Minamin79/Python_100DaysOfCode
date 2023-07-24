from data import MENU, resources

machine_is_on = True
order = input('What would you like? (espresso/latte/cappuccino)\n').lower()
money_given = 0
return_money = 0


def check_coins():
    global money_given
    global return_money
    
    print('Insert coins.')

    try:
        quarters = int(input('How many quarters: ')) * 25
        dimes = int(input('How many dimes?: ')) * 10
        nickles = int(input('How many nickles?: ')) * 5
        pennies = int(input('How many pennies?: '))

        money_given = (quarters + dimes + nickles + pennies) / 100
        if money_given >= MENU[order]['cost']:
            return_money = money_given - MENU[order]['cost']
            if return_money > 0:
                print(f"Here is your ${round(return_money, 2)} in change.")
            resources['money'] += money_given - return_money
            return 1
        else:
            resources['money'] = resources['money'] - money_given 
            print(f"You have to pay ${round(MENU[order]['cost'] - money_given, 2)} more.")
            return 0
    except:
        print('Invalid input')
        check_coins()


def check_resources():
    if check_coins() == 1:
        for item in MENU[order]['ingredients']:
            if MENU[order]['ingredients'][item] >= resources[item]:
                print(f'Sorry, there is not enough {item}.')
                return 0
            resources[item] = resources[item] - MENU[order]['ingredients'][item]
        return 1
    else:
        return 0
        

def order_coffee():
    global order
    global money_given
    global return_money
    
    if check_resources() == 1:
        print(f'Here is your {order}. Enjoy!')
    else:
        resources['money'] = (resources['money'] + return_money) - money_given
        print(f'${money_given} returned in general.')        
    order = input('What would you like? (espresso/latte/cappuccino)\n').lower()
                

while machine_is_on == True:
    if order != 'espresso' and order != 'latte' and order != 'cappuccino' and order != 'report' and order != 'off':
        print('Invalid input')
        order = input('What would you like? (espresso/latte/cappuccino)\n').lower()
    elif order == 'report':
        print(f"water: {resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {resources['money']}")
        order = input('What would you like? (espresso/latte/cappuccino)\n').lower()
    elif order == 'off':
        machine_is_on == False
    else:
        order_coffee()