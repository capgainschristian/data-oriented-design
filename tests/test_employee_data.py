import unittest

from ..employee_data.employee_data import EmployeeData

class TestEmployeeData(unittest.TestCase):
    def setUp(self):
        self.db = EmployeeData()