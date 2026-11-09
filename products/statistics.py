"""Calculate and display product statistics."""
from products.operations import display_products
from ui.menus import statistics_menu
from utils.helpers import CancelOperation, get_menu_choice


def total_number_of_items(product_list):
    """Return the total number of products."""
    return len(product_list)


def total_quantity_of_items(product_list):
    """Return the total quantity of all products."""
    total_quantity = 0
    for product in product_list:
        total_quantity += product['quantity']
    return total_quantity


def total_value_of_items(product_list):
    """Return the total value of all products."""
    total_value = 0
    for product in product_list:
        total_value += product['price'] * product['quantity']

    return total_value


def most_expensive_item(product_list):
    """Return the most expensive product."""
    if not product_list:
        return None
    most_expensive_product = product_list[0]

    for product in product_list:
        if product['price'] > most_expensive_product['price']:
            most_expensive_product = product

    return most_expensive_product


def least_expensive_item(product_list):
    """Return the least expensive product."""
    if not product_list:
        return None
    least_expensive_product = product_list[0]
    for product in product_list:
        if product['price'] < least_expensive_product['price']:
            least_expensive_product = product

    return least_expensive_product


def statistics(product_list):
    """Display product statistics menu and handle user choices."""
    try:
        if not product_list:
            print("Product list is empty")
            return
        while True:
            statistics_menu()
            statistics_menu_choice = get_menu_choice(0, 5)

            if statistics_menu_choice == 1:
                total_items = total_number_of_items(product_list)
                print(f" Total Items: {total_items}")

            elif statistics_menu_choice == 2:
                total_quantity = total_quantity_of_items(product_list)
                print(f"Total Quantity Items: {total_quantity}")

            elif statistics_menu_choice == 3:
                total_value = total_value_of_items(product_list)
                print(f"Total Value Products: {total_value}")

            elif statistics_menu_choice == 4:
                most_expensive_product = most_expensive_item(product_list)
                print("Most Expensive Product")
                display_products([most_expensive_product])

            elif statistics_menu_choice == 5:
                least_expensive_product = least_expensive_item(product_list)
                print("Least Expensive Product")
                display_products([least_expensive_product])

            elif statistics_menu_choice == 0:
                print("Back to Main Menu")
                break
    except CancelOperation:
        print("Returning to Main Menu")
