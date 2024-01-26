# tests/test_education_inquiry_package.py

import unittest
from inquirybot.education_inquiry.main import get_user_response

class TestEducationInquiryPackage(unittest.TestCase):
    def test_get_user_response(self):
        # Assuming you have a specific expected result for the test query
        expected_result = "Expected result for the test query"
        
        result = get_user_response("Test query")
        # Add assertions to check if the result is as expected
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
