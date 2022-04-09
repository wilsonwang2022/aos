import unittest
import aos_methods as methods

class MoodlePositiveTestCases(unittest.TestCase):

    @staticmethod # signal to Unittest framework that this is a function inside the class (vs. @classmethod)
    def test_aos(): # test_ in the name is mandatory
        methods.setUp()
        methods.validate_homepage_text()
        methods.validate_links()
        methods.validate_main_logo()
        methods.validate_contact_us_form()
        methods.validate_facebook()
        methods.validate_twitter()
        methods.validate_linkdin()
        methods.create_new_user()
        methods.check_user_created()
        methods.log_out()
        methods.log_in()
        methods.check_user_created()
        methods.delete_a_user()
        methods.verified_delete_user()
        methods.tearDown()

