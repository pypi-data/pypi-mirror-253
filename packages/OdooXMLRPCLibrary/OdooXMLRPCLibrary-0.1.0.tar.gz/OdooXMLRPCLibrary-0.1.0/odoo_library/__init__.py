from .create_rental import createRentalLibrary as CreateRentalLibrary
from .create_contact import createContactLibrary as CreateContactLibrary

# You can also instantiate the libraries if you want to provide pre-configured instances
create_rental_instance = CreateRentalLibrary()
create_contact_instance = CreateContactLibrary()

# Running the Flask apps by default when the package is imported
create_rental_instance.run()
create_contact_instance.run()