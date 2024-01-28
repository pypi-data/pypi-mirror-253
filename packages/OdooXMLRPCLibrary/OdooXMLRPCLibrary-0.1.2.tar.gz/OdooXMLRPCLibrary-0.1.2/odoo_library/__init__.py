from odoo_library.create_contact import CreateContactLibrary
from odoo_library.create_rental import CreateRentalLibrary

# You can also instantiate the libraries if you want to provide pre-configured instances

create_contact_instance = CreateContactLibrary()
create_rental_instance = CreateRentalLibrary()

# Running the Flask apps by default when the package is imported

create_contact_instance.run()
create_rental_instance.run()
