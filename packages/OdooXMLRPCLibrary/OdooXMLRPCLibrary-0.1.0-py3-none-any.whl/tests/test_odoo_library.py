# test_odoo_library.py

import unittest
from unittest.mock import patch
from odoo_library import CreateRentalLibrary, CreateContactLibrary

class TestCreateRentalLibrary(unittest.TestCase):
    def test_create_rental_order(self):
        # Mocking the Flask app's run method to avoid actually starting the server
        with patch.object(CreateRentalLibrary, 'run'):
            create_rental_instance = CreateRentalLibrary()

        # Add your test logic here, for example, make a request to the '/create_rental_order' endpoint
        # and assert the response

class TestCreateContactLibrary(unittest.TestCase):
    def test_create_contact(self):
        # Mocking the Flask app's run method to avoid actually starting the server
        with patch.object(CreateContactLibrary, 'run'):
            create_contact_instance = CreateContactLibrary()

        # Add your test logic here, for example, make a request to the '/create_contact' endpoint
        # and assert the response

if __name__ == '__main__':
    unittest.main()
