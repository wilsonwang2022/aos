import unittest
import aos_methods as methods

class MoodlePositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_aos(): # test_ in the name is mandatory
        methods.setUp()
        methods.create_new_user()
        methods.check_user_created()
        methods.log_out()
        methods.log_in()
        methods.check_user_created()
        methods.delete_a_user()
        methods.verified_delete_user()
        methods.tearDown()