class EmployeeData:
    def __init__(self):
        self.ids = []
        self.names = []
        self.salaries = []
        self.departments = []
        self.favorite_foods = []

    
    def add_employee(self, id, name, salary, department, favorite_food):
        if id in self.ids:
            print(f"Employee with ID {id} already exists.")
        else:
            self.ids.append(id)
            self.names.append(name)
            self.salaries.append(salary)
            self.departments.append(department)
            self.favorite_foods.append(favorite_food)
    
    def delete_employee(self, id):
        if id in self.ids:
            index = self.ids.index(id)
            self.ids.pop(index)
            self.names.pop(index)
            self.salaries.pop(index)
            self.departments.pop(index)
            self.favorite_foods.pop(index)
        else:
            print(f"Employee with ID {id} not found.")
    
    def update_employee(self, id, name=None, salary=None, department=None, favorite_food=None):
        if id in self.ids:
            index = self.ids.index(id)
            if name is not None:
                self.names[index] = name
            if salary is not None:
                self.salaries[index] = salary
            if department is not None:
                self.departments[index] = department
            if favorite_food is not None:
                self.favorite_foods[index] = favorite_food
        else:
            print(f"Employee with ID {id} not found.")
    def lookup_employee(self, id):
        if id in self.ids:
            index = self.ids.index(id)
            return {
                "id": self.ids[index],
                "name": self.names[index],
                "salary": self.salaries[index],
                "department": self.departments[index],
                "favorite food": self.favorite_foods[index],
            }
        else:
            print(f"Employee with ID {id} not found.")
            return None
        
    def employee_name_lookup(self, name):
        if name in self.names:
            index = self.names.index(name)
            return {
                "id": self.ids[index],
                "name": self.names[index],
                "salary": self.salaries[index],
                "department": self.departments[index],
                "favorite food": self.favorite_foods[index],
            }
        else:
            print(f"Employee with name {name} not found.")
            return None