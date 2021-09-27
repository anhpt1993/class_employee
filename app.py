from class_employee import Employee

the_anh = Employee("20110998", "Thế Anh", "Phạm", 15000000)

print(the_anh)

print("Bạn muốn tăng thêm bao nhiêu % lương: ")
percent = the_anh.get_percentage()
the_anh.raise_salary(percent)
print(the_anh)

