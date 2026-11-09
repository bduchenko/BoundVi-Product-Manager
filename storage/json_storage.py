import json
import os

from utils.helpers import get_menu_choice, CancelOperation
from utils.validators import validate_products


def remove_tmp(file):
    """Remove a temporary file if it exists."""
    try:
        os.remove(file)

    except FileNotFoundError:
        pass

    except OSError:
        print("file system error")


def save_products(product_list):
    """Save the product list to the main JSON file."""
    try:
        with open("products.json.tmp", "w", encoding="utf-8") as file:
            json.dump(product_list, file, indent=4, ensure_ascii=False)

    except PermissionError:
        print("No write access")
        remove_tmp("products.json.tmp")
        return False

    except OSError:
        print("File system error")
        remove_tmp("products.json.tmp")
        return False

    except TypeError:
        print("Data type error")
        remove_tmp("products.json.tmp")
        return False

    except ValueError:
        print("Data value error")
        remove_tmp("products.json.tmp")
        return False

    try:
        os.replace("products.json.tmp", "products.json")

    except OSError:
        print("file system error when overwriting a file from a temporary file")
        return False

    print("Save successful")
    return True


def load_products():
    """Load products from the main JSON file."""
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            file_list_products = json.load(file)
        if validate_products(file_list_products):
            return file_list_products
        else:
            return None

    except FileNotFoundError:
        print("File not found")
        return None

    except json.JSONDecodeError:
        print("Invalid or empty JSON file")
        return None


def load_backup():
    """Load and validate the backup file."""
    try:
        with open("products_backup.json", "r", encoding="utf-8") as file:
            backup_list = json.load(file)
        if validate_products(backup_list):
            return backup_list
        else:
            return None

    except FileNotFoundError:
        print("File not found")
        return None

    except json.JSONDecodeError:
        print("Invalid or empty JSON file")
        return None


def import_backup(product_list):
    """Import products from a backup file after user confirmation."""
    backup_list = load_backup()

    if backup_list is None:
        print("The backup file is corrupted")
        return

    try:
        while True:
            print("========IMPORT BACKUP=======")
            print("WARNING: Current product list will be replaced!")
            print("1. Confirm")
            print("2. Cancel")
            menu_number = get_menu_choice(1, 2)

            if menu_number == 1:
                if not save_products(backup_list):
                    print("Import failed")
                    break
                product_list[:] = backup_list
                print("The file has been overwritten with the backup version.")
                break

            elif menu_number == 2:
                print("Backup download cancelled")
                break

    except CancelOperation:
        print("Backup import cancelled")


def restore_from_backup():
    """Restore the product list from a backup file if the main file is corrupted."""
    try:
        while True:
            print("========RESTORE IMPORT BACKUP=======")
            print("The products file is corrupted; the program is terminating.")
            print("1. Restoring products from a backup")
            print("2. Exit Program")
            menu_number = get_menu_choice(1, 2)

            if menu_number == 1:
                backup_list = load_backup()

                if backup_list is None:
                    print("The backup file is corrupted; the program is exiting.")
                    return None

                elif not backup_list:
                    print("Backup list is empty")

                    while True:
                        print("Overwrite the file with an empty list?")
                        print("1. Confirm")
                        print("2. Cancel")
                        menu_number = get_menu_choice(1, 2)

                        if menu_number == 1:
                            if not save_products(backup_list):
                                print("Backup restoration failed.")
                                return None

                            print("The file has been overwritten with the backup version.")
                            return backup_list


                        elif menu_number == 2:
                            print("Backup download cancelled")
                            return

                else:
                    if not save_products(backup_list):
                        print("Backup restoration failed.")
                        return None

                    print("The file has been overwritten with the backup version.")
                    return backup_list

            elif menu_number == 2:
                print("Backup download cancelled")
                return None

    except CancelOperation:
        print("Backup import cancelled")
        return None


def export_backup(product_list):
    """Export the current product list to a backup JSON file."""
    with open("products_backup.json", "w", encoding="utf-8") as file:
        json.dump(product_list, file, indent=4, ensure_ascii=False)
        print("Backup file saved")