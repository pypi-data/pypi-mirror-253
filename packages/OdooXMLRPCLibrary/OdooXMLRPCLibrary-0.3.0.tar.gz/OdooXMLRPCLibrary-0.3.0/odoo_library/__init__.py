from odoo_library.create_contact import CreateContactLibrary
from odoo_library.saleOrderModel import SaleOrderModel

# You can also instantiate the libraries if you want to provide pre-configured instances

create_contact_instance = CreateContactLibrary()
create_sale_order_instance = SaleOrderModel()

# Running the Flask apps by default when the package is imported

create_contact_instance.run()
create_sale_order_instance.run()
