# All tests for R7 - logout go here

import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend logout page.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a sample user
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_Frontend0!')
)

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'price': '100'}
]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_logout_success(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_frontend@test.com")
        self.type("#password", "test_Frontend0!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        # logout
        self.click('a[href="/logout"]')
        #verify redirect to login page
        self.assertIn("Log In", self.driver.title)
        # open home page
        self.open(base_url)
        # verify redirect to login page
        self.assertIn("Log In", self.driver.title)
