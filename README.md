# BoundVi Product Manager

A Python-based application for managing products and inventory for BoundVi, a handmade leather accessories brand.

## Features

- Add, edit, and delete products.
- View and manage product information.
- Search and filter products.
- Track product quantities and prices.
- View inventory statistics.
- Store product data in JSON files.
- Create and restore data backups.
- Validate user input and handle errors.

## Technologies

- Python 3.13
- JSON
- Git

## Project Structure

```text
BoundVi_Product_Manager/
├── main.py
├── products.json
├── products_backup.json
├── products/
│   ├── __init__.py
│   ├── operations.py
│   └── statistics.py
├── storage/
│   ├── __init__.py
│   └── json_storage.py
├── ui/
│   ├── __init__.py
│   └── menus.py
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── validators.py
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/bduchenko/BoundVi-Product-Manager.git
   ```

2. Navigate to the project directory:

   ```bash
   cd BoundVi-Product-Manager
   ```

3. Run the application:

   ```bash
   python main.py
   ```

## Data Storage

Product information is stored locally in JSON files. The application also supports backup and restoration of product data.

## Project Status

This project is developed as a practical Python application and is continuously being improved.

---

**Author:** Bohdan Duchenko  
**GitHub:** [bduchenko](https://github.com/bduchenko)