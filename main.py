from users import Admin,Customer,Employee
from menu import Menu
from restaurent import Restaurent
from orders import Order
from fooditem import FoodItem

mama_res = Restaurent("Mama Restaurent") 

def Customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    customer = Customer(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add Item To Cart")
        print("3. View Cart")
        print("4. Pay Bill")
        print("5. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            customer.view_menu(mama_res)

        elif choice == 2:
            item_name = input("Enter Item Name : ")
            item_quantity = int(input("Enter Item Quantity : "))
            customer.add_to_cart(mama_res,item_name,item_quantity)

        elif choice == 3:
            customer.view_cart()
        
        elif choice == 4:
            customer.pay_bill()

        elif choice == 5:
            break

        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your Phone : ")
    address = input("Enter Your Address : ")
    admin = Admin(name=name,email=email,phone=phone,address=address)

    while True:
        print(f"Welcome {admin.name}")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Item")
        print("5. Delete Item")
        print("6. Exit")

        choice = int(input("Enter Your Choice : "))
        if choice == 1:
            item_name = input("Enter Item Name : ")
            item_price = int(input("Enter Item Price : "))
            item_quantity = int(input("Enter Item Quantity : "))
            item = FoodItem(item_name,item_price,item_quantity)
            admin.add_new_item(mama_res,item)

        elif choice == 2:
            name = input("Enter Employee Name : ")
            phone = input("Enter Employee Phone : ")
            email = input("Enter Employee Email : ")
            address = input("Enter Employee Address : ")
            designation = input("Enter Employee Designation : ")
            age = input("Enter Employee Age : ")
            salary = input("Enter Employee Salary : ")
            employee = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(mama_res,employee)

        elif choice == 3:
            admin.view_employee(mama_res)
        
        elif choice == 4:
            admin.view_menu(mama_res)

        elif choice == 5:
            item_name = input("Enter Item Name : ")
            admin.remove_item(mama_res,item_name)

        elif choice == 6:
            break

        else:
            print("Invalid Input")


while True:
    print("********* WELCOME *********")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        Customer_menu()

    elif choice == 2:
        admin_menu()

    elif choice == 3:
        break

    else:
        print("INVALID INPUT")