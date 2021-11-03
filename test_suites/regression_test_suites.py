import unittest

from tests.index.test_login import TestLogin
from tests.index.test_new_user import TestNewUser

login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
new_user = unittest.TestLoader().loadTestsFromTestCase(TestNewUser)

regression_suit = unittest.TestSuite([login, new_user])
unittest.TextTestRunner().run(regression_suit)