from abc import ABC
from orders import Order

# Creating user class:

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name=name
        self.phone=phone
        self.email=email
        self.address=address

class Customer(User):
    def __init__(self, name,email,phone,address):
        super(). __init__(name,phone,email,address)
        self.cart=Order()

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

    def add_to_cart(self,restaurent,item_name,quantity):
        item = restaurent.menu.find_item(item_name)
        if item:
            if quantity > item.quantity:
                print("Item Quantity Exceeded!")
            else:
                item.quantity = quantity
                self.cart.add_item(item)
                print("Item added")
        else:
            print("Item not found")

    def view_cart(self):
        print("******* VIEW CART *******")
        print("Name\tprice\tQuantity")
        for item,quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")
        print(f"Total Price:{self.cart.total_price}")

    def pay_bill(self):
        print(f"Total {self.cart.total_price} Paid Successfully!")
        self.cart.clear()


class Employee(User):
    def __init__(self,name,phone,email,address,age,designation,salary):
        super().__init__(name,phone,email,address)
        self.age=age
        self.designation=designation
        self.salary=salary

Emp= Employee("Rahim","r@gmail.com",136542368,"Dhaka",23,"chef",12000) 

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    #    self.employees=[]

    #def add_employee(self,name,phone,email,address,age,designation,salary):
    #    employee=Employee(name,phone,email,address,age,designation,salary)
    #    self.employees.append(employee)
    #    print(f"{name} is added!")

    def add_employee(self,restuarent,employee):
        restuarent.add_employee(employee)

    #def view_employee(self):
    #    print("Employee List!")
    #    for emp in self.employees:
    #        print(emp.name,emp.phone,emp.email,emp.address)

    def view_employee(self,restuarent):
        restuarent.view_employee()

    def add_new_item(self,restaurent,item):
        restaurent.menu.add_menu_item(item)

    def remove_item(self,restaurent,item):
        restaurent.menu.remove_item(item)

    def view_menu(self,restaurent):
        restaurent.menu.show_menu()

#ad = Admin("karim",1386553,"k@gmail.com","Dhaka")
#ad.add_employee("sagor","s@gmail.com",275346786,"khulna",21,"chef",12000)
#ad.view_employee()