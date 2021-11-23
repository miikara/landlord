import unittest
from service import BasicMenu
import mock

class TestService(unittest.TestCase):
    def setUp(self):
        self.basic_menu = BasicMenu()
   
    def test_prompt_closing_command():
        with mock.patch('builtins.input', return_value = '0'):
            assert basic_menu.prompt() == "Menu closed"

