# testing/test_generate_log.py

import os
import unittest
from datetime import datetime
from lib.generate_log import generate_log

class TestGenerateLog(unittest.TestCase):
    def setUp(self):
        self.log_data = ["Entry one", "Entry two", "Entry three"]
        self.filename = generate_log(self.log_data)

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_log_file_created(self):
        """Test that the log file is created with today's date in the filename."""
        self.assertTrue(os.path.exists(self.filename), f"{self.filename} not found.")

    def test_log_file_name_format(self):
        """Test that the filename follows the expected naming convention."""
        today = datetime.now().strftime("%Y%m%d")
        self.assertEqual(self.filename, f"log_{today}.txt", "Filename does not match expected format.")

    def test_log_file_content_matches_input(self):
        """Test that the content written to the log matches the input list."""
        with open(self.filename, "r") as file:
            lines = [line.strip() for line in file.readlines()]
        self.assertEqual(lines, self.log_data, "Log file contents do not match input data.")

    def test_generate_log_raises_error_on_invalid_input(self):
        """Test that the function raises a ValueError when input is not a list."""
        with self.assertRaises(ValueError):
            generate_log("This should be a list")

    def test_empty_log_list_creates_empty_file(self):
        """Test that passing an empty list still creates an empty log file."""
        filename = generate_log([])
        try:
            with open(filename, "r") as file:
                content = file.read()
            self.assertEqual(content, "")
        finally:
            if os.path.exists(filename):
                os.remove(filename)

if __name__ == "__main__":
    unittest.main()
