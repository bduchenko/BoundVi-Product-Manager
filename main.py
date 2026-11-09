from utils.helpers import get_menu_choice, CancelOperation
from storage.json_storage import (
    save_products,
    load_products,
    export_backup,
    import_backup,
    restore_from_backup
)
from products.operations import products_menu
from ui.menus import display_menu, data_management_menu
from products.statistics import statistics


def data_management(product_list):
    """Handle product data management operations."""
    try:
        while True:
            data_management_menu()
            data_menu_choice = get_menu_choice(0, 4)

            if data_menu_choice == 1:
                save_products(product_list)

            elif data_menu_choice == 2:
                loaded_products = load_products()
                if loaded_products is not None:
                    product_list[:] = loaded_products
                else:
                    print("Loading failed. Current data was not changed.")

            elif data_menu_choice == 3:
                export_backup(product_list)

            elif data_menu_choice == 4:
                import_backup(product_list)

            elif data_menu_choice == 0:
                print("Back to Main Menu")
                break

    except CancelOperation:
        print("Exit to main menu")


def main():
    """Run the BoundVi Product Manager application."""
    print("==============================")
    print("    BOUNDVI PRODUCT MANAGER   ")
    print("==============================")
    print("\nWelcome to BoundVi Product Manager!")
    try:
        products = load_products()
        if products is None:
            products_backup = restore_from_backup()
            if products_backup is None:
                return
            products = products_backup

        while True:
            display_menu()
            menu_choice = get_menu_choice(0, 3)

            if menu_choice == 1:
                products_menu(products)

            elif menu_choice == 2:
                statistics(products)

            elif menu_choice == 3:
                data_management(products)

            elif menu_choice == 0:
                print("Exit")
                break
    except CancelOperation:
        print("Operation cancelled. Exiting program")
        return

if __name__ == "__main__":
    main()





