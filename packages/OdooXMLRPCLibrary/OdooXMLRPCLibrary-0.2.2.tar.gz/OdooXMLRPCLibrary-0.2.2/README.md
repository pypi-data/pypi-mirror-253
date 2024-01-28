# OdooXMLRPCLibrary

OdooXMLRPCLibrary is a Python library that simplifies interaction with the Odoo ERP system using the XML-RPC API. It provides modules for creating contacts in the Odoo platform.

## Features

- Add and Manage contacts in the Odoo platform.

## Installation

To install the library, you can use pip:

```bash
pip install OdooXMLRPCLibrary
```

## How To Use?

**Importing**
```python
from odoo_library.create_contact import CreateContactLibrary

# Create instances of the libraries
create_contact_instance = CreateContactLibrary()

# Run the Flask apps
create_contact_instance.run()
```

**Code Usage**
```python
# Example code to create a Contact
data = {
    "odoo_server_url": "https://exampledb.odoo.com/",   # Your Odoo server URL here (with http or https)
    "database_name": "exampledb",                       # The database name on your Odoo Server 
    "odoo_username": "DB Username",                     # The username for your Odoo Database
    "odoo_password": "DB Password",                     # The password for your Odoo Database user
    "contact_name": "",                                 # Name of the contact
    "company_name": "",                                 # Company name of the contact
    "company_type": "company",                          # Type of company ("company" or "person")
    "address_type": "invoice",                          # Address type ("delivery" or "invoice")
    "street1": "Test Street 1",                         # First line of address
    "street2": "Test Street 2",                         # Second line of address (optional)
    "city": "Hyderabad",                                # City
    "state": "Telangana",                               # State
    "country": "India",                                 # Country
    "zip": "500032",                                    # Zip Code
    "gst_treatment": "",                                # GST Treatment if any ("registered" or "unregistered
    "vat": "",                                          # VAT number (if any)
    "job_position": "",                                 # Job Position (If applicable)
    "phone": "9988776655",                              # Phone Number
    "mobile": "",                                       # Mobile Number (Optional)
    "email": "Email@example.com",                       # Email ID
    "website": "https://example.com",                   # Website URL (Optional)
    "title": "",                                        # Title (Optional)
    "tags": ""                                          # Tags (Comma separated list, Optional)
}

response = create_contact_instance.create_contact(data)
return (response)
```


Feel free to paste this directly into your README.md file and customize it further if needed.
