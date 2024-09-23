class EmployeeDataController:
    def __init__(self, employee_data):
        self.employee_data = employee_data

    def get_all_employees(self):
        employees = []
        for i in range(len(self.employee_data.names)):
            employees.append(self.employee_data.names[i])

        return employees
    
    def get_total_employees(self):
        total = 0
        for i in range(len(self.employee_data.names)):
            total += 1
        return total
    
    def get_average_salary(self):
        avg_total = 0
        for i in range(len(self.employee_data.salaries)):
            avg_total += self.employee_data.salaries[i]
        return { "average salary": round(avg_total, 2)}
    
    def find_highest_lowest_salary(self):
        lowest = 0
        highest = 0
        for i in range(len(self.employee_data.salaries)):
            if self.employee_data.salaries[i] < lowest or lowest == 0:
                lowest = self.employee_data.salaries[i]
            elif self.employee_data.salaries[i] > highest:
                highest = self.employee_data.salaries[i]
        return {
            "lowest salary": round(lowest, 2),
            "highest salary": round(highest, 2),
        }
    
    def get_total_salaries(self):
        total = 0
        for i in range(len(self.employee_data.salaries)):
            total += self.employee_data.salaries[i]
        return {"total salaries": round(total, 2)}
