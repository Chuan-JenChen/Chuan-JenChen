hrsworked= int(input("How many hours have you worked?"))
if hrsworked<60:
    salary=120*hrsworked
    print(salary)
elif hrsworked>=60 and hrsworked<80:
    salary=120*1.25*(hrsworked)
    print(salary)
elif hrsworked>=80:
    salary=120*1.5*(hrsworked)
    print(salary)
else:
    print("輸入錯誤")



