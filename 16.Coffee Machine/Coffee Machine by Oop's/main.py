import coffee_maker
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_money = MoneyMachine()
my_coffee_maker = CoffeeMaker()
my_menu = Menu()
is_on = True

while is_on:
    options = my_menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money.report()
    else:
        drink = my_menu.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)