# OdooXMLRPCLibrary

OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using the XML-RPC API. It provides modules for creating rental orders and contacts in the Odoo platform.

## Features

- Create rental orders with specified details.
- Manage contacts in the Odoo platform.

## Installation

To install the library, you can use pip:

```bash
pip install OdooXMLRPCLibrary
```

**Usage**
```bash
from OdooXMLRPCLibrary import CreateRentalLibrary, CreateContactLibrary

# Create instances of the libraries
create_rental_instance = CreateRentalLibrary()
create_contact_instance = CreateContactLibrary()

# Run the Flask apps
create_rental_instance.run()
create_contact_instance.run()
```

**Configuration**
```bash
data = {
    'customer_id': 1,
    'product_id': [1, 2, 3],
    'start_date': '2022-01-01',
    'end_date': '2022-01-10',
    'quantity': [5, 3, 2],
    'odoo_server_url': 'https://your-odoo-instance.com',
    'database_name': 'your_odoo_database',
    'odoo_username': 'your_odoo_username',
    'odoo_password': 'your_odoo_password',
    'gst_treatment': 'GST Treatment',
}

response = create_rental_instance.create_rental_order(data)
print(response)
```

```bash
# Example code to create a rental order
data = {
    'customer_id': 1,
    'product_id': [1, 2, 3],
    'start_date': '2022-01-01',
    'end_date': '2022-01-10',
    'quantity': [5, 3, 2],
    'odoo_server_url': 'https://your-odoo-instance.com',
    'database_name': 'your_odoo_database',
    'odoo_username': 'your_odoo_username',
    'odoo_password': 'your_odoo_password',
    'gst_treatment': 'GST Treatment',
}

response = create_rental_instance.create_rental_order(data)
print(response)
```


Feel free to paste this directly into your README.md file and customize it further if needed.
