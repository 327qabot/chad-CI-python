import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class BuyTicket(BaseCase):

    def register(self):
        """register new user"""
        self.open(base_url + '/register')
        self.type("#email", "test_integration@test.com")
        self.type("#name", "test0")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def login(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test_integration@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def sell_ticket(self):
        """ Add a ticket to be sold """
        self.open(base_url + '/')
        self.type("#sell_name", "Avengers")
        self.type("#sell_quantity", "3")
        self.type("#sell_price", "35")
        self.type("#sell_exp_date", "2022\t12-20")
        self.click("#sell_submit")

    def logout(self):
        """ Logout of user we used to create ticket """
        self.open(base_url + '/logout')

    def register2(self):
        """register new user to buy ticket """
        self.open(base_url + '/register')
        self.type("#email", "test_integration2@test.com")
        self.type("#name", "test2")
        self.type("#password", "Test0!qwertyuiop")
        self.type("#password2", "Test0!qwertyuiop")
        self.click('input[type="submit"]')

    def login2(self):
        """ Login to Swag Labs and verify that login was successful. """
        self.open(base_url + '/login')
        self.type("#email", "test_integration2@test.com")
        self.type("#password", "Test0!qwertyuiop")
        self.click('input[type="submit"]')
    
    def buy_ticket(self):
        """ Add a ticket to be sold """
        self.open(base_url + '/')
        self.click("#ticket-avengers-buy", timeout=5)
        self.click("#buy_submit", timeout=5)

    def test_buy_ticket(self):
      """ This test checks the implemented sell 
      ticket feature """
      self.register()
      self.login()
      self.sell_ticket()
      self.logout()
      self.register2()
      self.login2()
      self.buy_ticket()
      self.open(base_url + "/")
      self.assert_element_absent("#ticket-Avengers")
      
