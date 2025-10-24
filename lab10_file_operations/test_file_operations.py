"""
Mohammed Azhar
Oct 15, 2025
Lab 9, file operation test
"""

import unittest
import os
from file_operations import read_file, write_file, append_file, email_read

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        #set up temporary test file name before each test
        self.filename = "test_file.txt"
        self.msg = "MOhammed Azhar"

    def tearDown(self):
        # remove the test file after each test
        if os.path.exists(self.filename):
            os.remove(self.filename)
        
    def test_write_file(self):
        #test writing text to a file
        msg = "Mohammed Azhar"
        write_file(self.filename, msg)

        #verify the file exists and content matches
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as f:
            result = f.read()

        self.assertEqual(result, msg)

    def test_read_file(self):
        #test reading text from a file
        expected_content = "Read me!"
        with open(self.filename, "w") as f:
            f.write(expected_content)

        data = read_file(self.filename)
        self.assertEqual(data, expected_content)

    def test_append_file(self):
        #test appending text to an existing file
        initial_content = "line one"
        append_content = "\nLinetwo"
        
        with open(self.filename, "w") as f:
            f.write(initial_content)
        append_file(self.filename, append_content)

        with open(self.filename, "r") as f:
            final_data = f.read()

        self.assertEqual(final_data, initial_content + append_content)


#Lab Exercise
def test_email_read(self):
        #test read mode of email_read function
        email_file = "test_emails.txt"
        with open(email_file, "w") as f:
            f.write("mohammed@gmail.com\n")
            f.write("azhar@yahoo.com\n")
            f.write("someone@gmail.com\n")

        result = email_read(email_file, "@gmail")
        self.assertEqual(result, 2)

        if os.path.exists(email_file):
            os.remove(email_file)


#run the unit tests automatically when the file is run
if __name__ == "__main__":
    unittest.main()