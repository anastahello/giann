class employee:
    def __init__(self,firstname,lastname,email,salary,years):
       self.firstname=firstname
       self.lastname=lastname
       self.email=email
       self.salary=salary
       self.years=years

    

    def display(self):
        print(self.firstname)
        print(self.lastname)
        print(self.email)
        print(self.salary)
        print(self.years)
     


e1=employee("anastasia","asla","anasta@fgtt.com",5000,1)
e2=employee("dhmhtrhs","arapoglou","dimi@fgtt.com",6000,15)
e3=employee("giannhs","drosos","gidro@fgtt.com",3890,7)
e4=employee("kleio","souratsakh","soyrakli@fgtt.com",8600,20)

e1.display()
print("\n")
e2.display()
print("\n")
e3.display()
print("\n")
e4.display()

print(len(e2.firstname)+ len(e2.lastname))
employees ={e1,e2,e3,e4}
for employee in employees:
  if employee.years > 4:
   employee.salary+=300
  print(employee.salary)  
  


 


        