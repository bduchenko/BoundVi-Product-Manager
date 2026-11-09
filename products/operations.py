"""Handle product management operations."""
import math
import random
from storage.json_storage import save_products
from ui.menus import display_products_menu, edit_product_menu
from utils.helpers import get_menu_choice, get_input, CancelOperation


def display_products(product_list):
    """Display all products in the list."""
    if not product_list:
        print("No products found")
        return

    for product in product_list:
        print("===================="
              f"\nID: {product['id']}"
              f"\nName: {product['name']}"
              f"\nPrice: {product['price']}"
              f"\nQuantity: {product['quantity']}"
              f"\nCategory: {product['category']}"
              "\n====================\n"
              )


def find_product(product_list):
    """Find a product by its name."""
    find_name = get_input("Enter name for search")
    for product in product_list:
        if find_name.strip().lower() == product['name'].strip().lower():
            print("product found")
            return product
    else:
        print("Product not found")
        return None


def search_product(product_list):
    """Search for a product and display the result."""
    search_name = find_product(product_list)
    if search_name is not None:
        display_products([search_name])


def duplicate_exist(name, product_list, current_product=None):
    """Check whether a product name already exists."""
    for product in product_list:
        if product is not current_product:
            if product['name'].lower().strip() == name.lower().strip():
                return True

    return False


def generate_unique_id(product_list):
    """Generate a unique ID for a new product."""
    counter_add_id = 0

    while True:
        if counter_add_id >= 100:
            print("No free one found ID")
            return None
        add_id = random.randint(1000, 999999)

        for product in product_list:
            if add_id == product['id']:
                counter_add_id += 1
                break
        else:
            return add_id


def add_product(product_list):
    """Add a new product to the product list."""
    try:
        while True:
            try:
                add_name = get_input("Enter name product")
                if duplicate_exist(add_name, product_list):
                    raise ValueError("This item is already in the list.")
                break
            except ValueError as error:
                print(error)
                print("Enter valid name")

        while True:
            try:
                add_price = float(get_input("Enter price"))
                if not math.isfinite(add_price) or add_price <= 0:
                    raise ValueError("Price must be greater than 0")
                break
            except ValueError as error:
                print(error)
                print("Enter valid price")

        while True:
            try:
                add_quantity = int(get_input("Enter quantity"))
                if add_quantity < 0:
                    raise ValueError("Quantity must be greater than or equal to 0")
                break
            except ValueError as error:
                print(error)
                print("Enter valid quantity")

        while True:
            try:
                add_category = get_input("Enter category")
                if not add_category.strip():
                    raise ValueError("Category empty")
                break
            except ValueError as error:
                print(error)
                print("Enter valid category")

        add_id = generate_unique_id(product_list)
        if add_id is not None:
            print(f"Automatically assigned ID - {add_id}")
            new_product = {
                "id": add_id,
                "name": add_name,
                "price": add_price,
                "quantity": add_quantity,
                "category": add_category
            }
            product_list.append(new_product)
            save_products(product_list)
            print("Product added to the list")
    except CancelOperation:
        print("Adding product cancelled")


def editing_name_product(product_list, product):
    """Edit the name of an existing product."""
    while True:
        print("===Edit Name===")
        try:
            edit_name = get_input("Enter name for editing")
            if duplicate_exist(edit_name, product_list, current_product=product):
                raise ValueError("This item is already in the list.")
            product['name'] = edit_name
        except ValueError as error:
            print(error)
            print("Enter valid name")
        else:
            print("Name Product Edited")
            break


def editing_price_product(product):
    """Edit the price of an existing product."""
    while True:
        print("===Edit Price===")
        try:
            edit_price = float(get_input("Enter price for editing"))
            if not math.isfinite(edit_price) or edit_price <= 0:
                raise ValueError("The price must be greater than 0")
            product['price'] = edit_price
        except ValueError as error:
            print(error)
            print("Enter valid Price")
        else:
            print("Price Product Edited")
            break


def editing_quantity_product(product):
    """Edit the quantity of an existing product."""
    while True:
        print("===Edit Quantity===")
        try:
            edit_quantity = int(get_input("Enter quantity for editing"))
            if edit_quantity < 0:
                raise ValueError("The quantity must be greater than or equal to 0.")
            product['quantity'] = edit_quantity
        except ValueError as error:
            print(error)
            print("Enter valid Quantity")
        else:
            print("Quantity Product Edited")
            break


def editing_category_product(product):
    """Edit the category of an existing product."""
    while True:
        print("===Edit Category===")
        try:
            edit_category = get_input("Enter category for editing")
            product['category'] = edit_category
        except ValueError as error:
            print(error)
            print("Enter valid Category")
        else:
            print("Category Product Edited")
            break


def products_menu(product_list):
    """Display and handle the products menu."""
    try:
        while True:
            display_products_menu()
            products_menu_choice = get_menu_choice(0, 5)

            if products_menu_choice == 1:
                display_products(product_list)

            elif products_menu_choice == 2:
                search_product(product_list)

            elif products_menu_choice == 3:
                add_product(product_list)

            elif products_menu_choice == 4:
                edit_product(product_list)

            elif products_menu_choice == 5:
                delete_product(product_list)

            elif products_menu_choice == 0:
                print("Back to Main Menu")
                break
    except CancelOperation:
        print("Return to Main Menu")


def edit_product(product_list):
    """Edit the details of an existing product."""
    try:
        product_for_edit = find_product(product_list)
        if product_for_edit is not None:
            display_products([product_for_edit])
            while True:
                edit_product_menu()
                edit_menu_number = get_menu_choice(0, 4)

                if edit_menu_number == 1:
                    editing_name_product(product_list, product_for_edit)
                    save_products(product_list)

                elif edit_menu_number == 2:
                    editing_price_product(product_for_edit)
                    save_products(product_list)

                elif edit_menu_number == 3:
                    editing_quantity_product(product_for_edit)
                    save_products(product_list)

                elif edit_menu_number == 4:
                    editing_category_product(product_for_edit)
                    save_products(product_list)

                elif edit_menu_number == 0:
                    print("Back to Products Menu")
                    break
    except CancelOperation:
        print("Editing cancelled")


def delete_product(product_list):
    """Delete a product after user confirmation."""
    try:
        product_for_delete = find_product(product_list)
        if product_for_delete is not None:
            display_products([product_for_delete])
            while True:
                print("========Delete Product=======")
                print("Do you confirm the deletion?")
                print("1. Yes")
                print("2. No")
                menu_delete = get_menu_choice(1, 2)

                if menu_delete == 1:
                    product_list.remove(product_for_delete)
                    save_products(product_list)
                    print("Product deleted")
                    break
                elif menu_delete == 2:
                    print("Deletion cancelled")
                    break

    except CancelOperation:
        print("Deletion cancelled")

