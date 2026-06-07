# Import drink recipes and machine resources
import requirements

# Store available machine resources
resource = requirements.Resources


# Display current machine resources
def report(resource):
    return(f'''The available resources are
water: {resource['water']}ml
milk: {resource['milk']}ml
coffee: {resource['coffee']}''')


# Determine which drink the user selected
def drink():
    if user_input == '1':
        return requirements.Espresso
    elif user_input == '2':
        return requirements.Latte
    elif user_input == '3':
        return requirements.Cappuccino
    return None


# Collect money from the user using coin inputs
def money_input():
    pennies = int(input("How many pennies? "))
    nickels = int(input("How many nickels? "))
    dimes = int(input("How many dimes? "))
    quarters = int(input("How many quarters? "))

    # Calculate total money inserted
    return pennies*0.01 + nickels*0.05 + dimes*0.10 + quarters*0.25


# Check whether enough resources are available
# and process the drink purchase
def resources_available(drink):

    if drink['water'] <= resource['water'] and \
       drink['coffee'] <= resource['coffee'] and \
       drink['milk'] <= resource['milk']:

        # Request payment from user
        money_given = money_input()

        # Continue requesting money until full payment is made
        while money_given < drink['price']:
            print(
                f"Your chosen drink costs ${drink['price']}. "
                f"Please add more ${round(drink['price'] - money_given, 2)}"
            )

            money_given += money_input()

        # Deduct ingredients from machine resources
        resource['water'] -= drink['water']
        resource['coffee'] -= drink['coffee']
        resource['milk'] -= drink['milk']

        # Complete transaction and return change
        if money_given >= drink['price']:
            return_amt = money_given - drink['price']

            print(
                f"Your drink is ready! Enjoy your {drink['name']}!!"
            )

            print(
                f"Here is your change {round(return_amt, 2)}."
            )

    else:
        print("Not enough resources!")

        # Inform user which resources are insufficient
        if drink['water'] > resource['water']:
            print("Add more water!")

        if drink['coffee'] > resource['coffee']:
            print("Add more coffee!")

        if drink['milk'] > resource['milk']:
            print("Add more milk!")


# Main machine loop
stop = False

while not stop:

    user_input = input(
        "What is your choice? Espresso [1], Latte [2] or Cappuccino [3]\n"
    )

    # Generate resource report
    if user_input.lower() == 'report':
        print(report(resource))

    # Stop the machine
    elif user_input.lower() == 'stop':
        print("Machine Stopped!")
        stop = True

    # Process drink selection
    else:
        your_drink = drink()

        if your_drink:
            resources_available(your_drink)
        else:
            print('invalid_selection')