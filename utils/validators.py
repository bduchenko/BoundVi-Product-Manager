"""Validate product data before using or saving it."""
def validate_products(product_list):
    """Check whether the product list contains valid product data."""
    if not isinstance(product_list, list):
        print("Invalid product data")
        return None

    required_keys = {"id", "name", "price", "quantity", "category"}

    for product in product_list:
        if not isinstance(product, dict):
            print("Invalid product data")
            return None
        if not all(key in product for key in required_keys):
            print("Invalid product data")
            return None

        if not (
            not isinstance(product["price"], bool)
            and isinstance(product["price"], (float, int))
            and not isinstance(product["id"], bool)
            and isinstance(product["id"], int)
            and not isinstance(product["quantity"], bool)
            and isinstance(product["quantity"], int)
            and isinstance(product["name"], str)
            and isinstance(product["category"], str)
        ):
            print("Invalid product data")
            return None

        if product["price"] < 0:
            print("Price invalid")
            return None
        if product["quantity"] < 0:
            print("Quantity invalid")
            return None
        if product["id"] <= 0:
            print("ID invalid")
            return None
        if not product["name"].strip():
            print("Name empty")
            return None
        if not product["category"].strip():
            print("Category empty")
            return None

    return True

