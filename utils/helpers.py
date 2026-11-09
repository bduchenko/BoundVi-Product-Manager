class CancelOperation(Exception):
    """Exception raised when the user cancels an operation."""
    pass


def get_input(prompt):
    """Get user input and handle empty values or cancellation."""
    entered_data = input(prompt).strip()
    if entered_data.lower() == "cancel":
        raise CancelOperation
    if not entered_data:
        raise ValueError("Input cannot be empty")

    return entered_data


def get_menu_choice(min_value, max_value, prompt="Enter menu number"):
    """Get and validate a menu choice within the specified range."""
    while True:
        try:
            menu_choice = int(get_input(prompt))
            if not min_value <= menu_choice <= max_value:
                raise ValueError

            return menu_choice

        except ValueError:
            print("Invalid menu number")

