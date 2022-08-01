from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# def obtain_drink_information():
#     for item in menu_information.menu:
#         if item.name == drink:
#             return item.cost

menu_information = Menu()
coffee_machine = CoffeeMaker()
money_matters = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"​What would you like? ({menu_information.get_items()}) ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_machine.report()
        money_matters.report()
        # print(f"Money: ${money_matters.profit}")
    else:
        details_of_drink = menu_information.find_drink(choice)
        if coffee_machine.is_resource_sufficient(details_of_drink):
           if money_matters.make_payment(details_of_drink.cost):
               coffee_machine.make_coffee(details_of_drink)
            
            
                    

# print(menu_information.menu)
# latte = menu_information.menu[0].name
# print(latte)