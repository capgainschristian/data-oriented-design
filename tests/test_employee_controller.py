import unittest
from unittest.mock import MagicMock
from employee_data.employee_data import EmployeeData
from controllers.employee_controller import EmployeeDataController

class TestEmployeeDataController(unittest.TestCase):
    def setUp(self):
        self.mock_employee_data = MagicMock(spec=EmployeeData)
        
        self.mock_employee_data.salaries = [60000, 75000, 50000, 90000]
        self.mock_employee_data.__len__.return_value = len(self.mock_employee_data.salaries)
    
        self.mock_employee_data.__iter__.return_value = iter([
            {"id": 1, "name": "Alice", "salary": 60000, "department": "IT", "favorite food": "Pizza"},
            {"id": 2, "name": "Bob", "salary": 75000, "department": "Finance", "favorite food": "Sushi"},
            {"id": 3, "name": "Charlie", "salary": 50000, "department": "HR", "favorite food": "Burger"},
            {"id": 4, "name": "David", "salary": 90000, "department": "Sales", "favorite food": "Steak"},
        ])

        self.controller = EmployeeDataController(self.mock_employee_data)

    def test_get_all_employees(self):
        with unittest.mock.patch("builtins.print") as mocked_print:
            self.controller.get_all_employees()
            self.assertEqual(mocked_print.call_count, 4)
    
    def test_get_total_employees(self):
        self.assertEqual(self.controller.get_total_employees(), 4)

    def test_get_average_salary(self):
        expect_avg_salary = sum(self.mock_employee_data.salaries) / len(self.mock_employee_data.salaries)
        self.assertEqual(self.controller.get_average_salary(), {"average salary": round(expect_avg_salary, 2)})

    def test_find_highest_lowest_salary(self):
        expected_highest = max(self.mock_employee_data.salaries)
        expected_lowest = min(self.mock_employee_data.salaries)
        self.assertEqual(
            self.controller.find_highest_lowest_salary(),
            {"lowest salary": round(expected_lowest, 2), "highest salary": round(expected_highest, 2)}
        )

    def test_get_total_salaries(self):
        expected_total = sum(self.mock_employee_data.salaries)
        self.assertEqual(self.controller.get_total_salaries(), {"total salaries": round(expected_total, 2)})
