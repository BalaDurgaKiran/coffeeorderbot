from utils import print_message, get_size, order_latte

def order_mocha():
    while True:
        res = input("Would you like to try our limited-edition peppermint mocha?\n[a] Sure!\n[b] Maybe next time!\n> ")
        if res == 'a':
            return 'peppermint mocha'
        elif res == 'b':
            return 'mocha'
        print_message()

def get_drink_type():
    res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return order_mocha()
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def coffee_bot():
    print('Welcome to the cafe!')

    order_drink = 'y'
    drinks = []

    while order_drink.lower() in ['y', 'yes', 'sure']:
        size = get_size()
        drink_type = get_drink_type()
        drink = '{} {}'.format(size, drink_type)
        print('Alright, that\'s a {}!'.format(drink))
        drinks.append(drink)

        while True:
            order_drink = input("Would you like to order another drink? (y/n)\n> ").lower()
            if order_drink in ['y', 'n', 'yes', 'sure', 'nah', 'no']:
                break
            elif order_drink in ['stop', 'bye']:
                order_drink = 'n'
                break
            print_message()

    print("Okay, so I have:")
    for drink in drinks:
        print("- " + drink)

    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your order will be ready shortly.'.format(name))

# Run the chatbot
coffee_bot()
