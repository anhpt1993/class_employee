class Employee:
    def __init__(self, ID = "", first_name = "", surname = "", salary = 0):
        self.ID = ID
        self.first_name = first_name
        self.surname = surname
        self.salary = salary

    def get_percentage(self):
        while True:
            try:
                percent = float(input())
                if percent > 0:
                    return percent
                else:
                    print("\nInvalid Value. Try Again!!!\n")
            except ValueError:
                print("\nInvalid Value. Try Again!!!\n")

    def get_fullname(self):
        return self.first_name + " " + self.surname

    def get_salary(self, new_salary):
        return self.salary

    def get_annual_salary(self):
        return self.salary * 12

    def raise_salary(self, percent):
        self.salary = self.salary * (1 + percent / 100)

    def __str__(self):
        return f"""
                +) {"ID":15} : {self.ID}
                +) {"Full name":15} : {self.get_fullname()}
                +) {"Salary":15} : {self.salary:.0f} VND
                +) {"Annual Salary":15} : {self.get_annual_salary():.0f} VND
                """