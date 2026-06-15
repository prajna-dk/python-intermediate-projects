# Import the required classes that manage the menu,
# coffee resources, and payment processing.
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Create objects from each class
your_menu = Menu()
your_coffee = CoffeeMaker()
your_money_processing = MoneyMachine()

# Keep the coffee machine running until the user stops it
machine_on = True

while machine_on:

    # Display all available drinks
    print(your_menu.get_items())

    # Get the user's drink selection
    user_choice = input("Your choice: ").lower()

    # Check whether the selected drink exists on the menu
    if user_choice in your_menu.get_items():

        # Retrieve the selected drink object
        drink = your_menu.find_drink(user_choice)

        # Verify that sufficient ingredients are available
        if your_coffee.is_resource_sufficient(drink):

            # Process payment before preparing the drink
            if your_money_processing.make_payment(drink.cost):

                # Prepare and serve the selected coffee
                your_coffee.make_coffee(drink)

    # Display machine resource and financial reports
    elif user_choice == 'report':
        your_coffee.report()
        your_money_processing.report()

    # Turn off the coffee machine
    elif user_choice == 'stop':
        machine_on = False
        print("Machine is turned off!")

    # Handle invalid user input
    else:
        print("Not a valid choice!")