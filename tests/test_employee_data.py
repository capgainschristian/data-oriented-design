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

    def test_add_duplicate_employee_id(self):
        self.db.add_employee(1, "Alice", 60000, "IT", "Pizza")
        with self.assertRaises(ValueError):
            self.db.add_employee(1, "Bob", 70000, "Finance", "Sushi")
    
    def test_add_invalid_department(self):
        with self.assertRaises(ValueError):
            self.db.add_employee(2, "Charlie", 50000, "Engineering", "Burgers")

    def test_delete_employee(self):
        self.db.add_employee(3, "David", 90000, "HR", "Steak")
        self.db.delete_employee(3)
        self.assertEqual(len(self.db), 0)
        self.assertIsNone(self.db.lookup_employee(3))

    def test_delete_non_existent_employee(self):
        self.assertIsNone(self.db.delete_employee(99))

    def test_update_employee(self):
        self.db.add_employee(4, "Eve", 70000, "Marketing", "Salad")
        self.db.update_employee(4, salary=75000, department="Sales")
        updated_employee = self.db.lookup_employee(4)
        self.assertEqual(updated_employee["salary"], 75000)
        self.assertEqual(updated_employee["department"], "Sales")

    def test_update_on_nonexistent_employee(self):
        self.db.update_employee(99, salary=80000)
    
    def test_lookup_employee(self):
        self.db.add_employee(5, "Frank", 50000, "Operations", "Pasta")
        employee = self.db.lookup_employee(5)
        self.assertEqual(employee["name"], "Frank")
        self.assertEqual(employee["salary"], 50000)
    
    def test_lookup_nonexistent_employee(self):
        self.assertIsNone(self.db.lookup_employee(100))
    
    def test_employeee_name_lookup(self):
        self.db.add_employee(6, "Zoe", 120000, "Finance", "Tacos")
        employee  = self.db.employee_name_lookup("Zoe")
        self.assertEqual(employee["name"], "Zoe")
        self.assertEqual(employee["favorite food"], "Tacos")

    def test_employee_name_lookup_nonexistent(self):
        self.assertIsNone(self.db.employee_name_lookup("Bob"))

    def test_len(self):
        self.db.add_employee(7, "Hank", 20000, "IT", "Soup")
        self.db.add_employee(8, "Ivy", 300000, "HR", "Ice Cream")
        self.assertEqual(len(self.db), 2)
    
    def test_iter(self):
        self.db.add_employee(9, "Jack", 62000, "Sales", "Fish")
        employees = list(iter(self.db))
        self.assertEqual(len(employees), 1)
        self.assertEqual(employees[0]["name"], "Jack")
