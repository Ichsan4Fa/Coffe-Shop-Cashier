"""
Docstring for Coffee_cashier.coffee

A Project that simulates coffee order system in coffee shop. This project will implement tuples and dictionaries for menus. 
For the scenario, customers will choose the menu, then system will calculate total prices from checkout menu. Customers may only
choose one menu.

Idea from : Tulus Setiawan (TikTok)
"""

# Coffee shop and menus
coffee_shop = "This Is Kafein"
shop_menus = ("Espresso", "Cappucino", "Machiato", "Latte") # Tuple for unchangable values

# Dictionary for price list
price_list = {
    "Espresso":12000,
    "Cappucino":15000,
    "Machiato":20000,
    "Latte":22000
}

# Define price calculator method
def calculate_price(price_per_menu, quantity):
    tax = 0.1
    service_fee = 0.2
    total = price_per_menu * quantity
    if(quantity >= 3):
        total = total - price_per_menu # Buy 2 get 1 free
    total = total + (total * tax) + (total * service_fee)
    return float(total)

#----- MAIN -----

print(f"############# WELCOME TO {coffee_shop.upper()} #############")
basket_menu = []# List all selected menu
try:
    print("Please choose a menu below: ")
    for i, coffee in enumerate(shop_menus, 1):
        print(f"{i}. {coffee} - Rp.{price_list[coffee]}")
    selected_menu = int(input("\nType number for choosing menu: "))
    qty = int(input(f"How many cups did you order?"))

    if 1 <= selected_menu <= len(shop_menus):
        menu = shop_menus[selected_menu - 1]
        price = price_list[menu]

        total_price = calculate_price(price, qty)

        basket_menu.append(menu)

        print(f"\nShop Details: {basket_menu}")
        print(f"\nTax: 10%")
        print(f"\nService Fee: 20%")
        print(f"Total Price: {total_price}")
    else:
        print(f"Sorry, we don't have that menu")
except ValueError:
    print(f"Please type valid menu number and valid quantity")
print("Thank you for shopping with us :)")
