import unittest

from tests.index.test_login import TestLogin
from tests.index.test_new_user import TestNewUser
from tests.index.test_file_upload import TestFileUpload

login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
new_user = unittest.TestLoader().loadTestsFromTestCase(TestNewUser)
file_upload = unittest.TestLoader().loadTestsFromTestCase(TestFileUpload)
regression_suit = unittest.TestSuite([login, new_user, file_upload])

unittest.TextTestRunner().run(regression_suit)