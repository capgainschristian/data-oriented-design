import unittest

from employee_data.employee_data import EmployeeData


class TestEmployeeData(unittest.TestCase):
    def setUp(self):
        self.db = EmployeeData()

    def test_add_employee(self):
        self.db.add_employee(1, "Alice", 60000, "IT", "Pizza")
        self.assertEqual(len(self.db), 1)
        self.assertEqual(self.db.lookup_employee(1), {
            "id": 1,
            "name": "Alice",
            "salary": 60000,
            "department": "IT",
            "favorite food": "Pizza",
        })