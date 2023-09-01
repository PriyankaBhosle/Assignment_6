# Admin will have the following functionalities
import json
class Admin():
    def __init__(self):
        self.food_id=0
        self.food_item={}

    def Add_new_food(self):
        self.food_id+=1
        Name = input("Enter Food Name:")
        Quantity = input("Enter Food Quantity:")
        Stock = input("Enter Food Stock:")
        Price = float(input("Enter Food Price:"))
        Discount= float(input("Enter Food Discount:"))
        food_item={"Food name":Name, "Food quantity":Quantity, "Stock":Stock, "Food price":Price, "Food Discount":Price-(Price*Discount/100)}
        self.food_item[self.food_id]=food_item
        with open("food_item.json","w")as f:
            json.dump(self.food_item,f,indent=4)
            print("Food item added successfully!")
        return self.food_item
    

    def Edit_food_items(self):
        with open("food_item.json","r")as f:
            data=json.load(f)
        for k,v in data.items():
            print(f"food_id:{k}||food_item:{v}")
        id= int(input("Enter the food id which you want to edit:"))
        item=int(input("Enter the food id which you want to edit: "))
        Updated_item = input("Enter the updated value")
        data[id][item]=Updated_item
        with open("food_item.json","w")as f:
            json.dump(data,f,indent=4)
            print("Food items added successfully!")
        return data
    
    def Remove_food_items(self):
        with open("food_item.json","r")as f:
            data=json.load(f)
        for k,v in data.items():
            print(f"food_id:{k}||food_items:{v}")
        id = int(input("Enter the food id which you want to delete:"))
        del= data[id]
        with open("food-item.json","w")as f:
            json.dump(data,f,indent=4)
            print("Food items deleted successfully!")
        return data
x=Admin()
print(x.Add_new_food())
print(x.Edit_food_items())
print(x.Remove_food_items())


# The user will have the following functionalities: 


class user:
    def __init__(self):
        self.personal_details={}
        self.email={}
        self.password={}    
    def Register(self):
        Name=input("Enter your name:")
        Phone_number=int(input("Enter your phone number:"))
        self.email=input("Enter your email:")
        Address=input("Enter your address:")
        self.password=input("Enter your Password:")
        self.personal_details={"Name":Name, "Phone number":Phone_number, "Email":self.Email,"Address":Address, "Password":self.password}
        with open("personal_details.json","w")as f:
            json.dump(self.personal_details,f,indent=4)
            print("Congratulations acoount created")
        return self.personal_details
    def Login(self):
        print("Welcome to your login page...")
        with open("self.personal_details", "r")as f:
            data=json.load(f)
        while True:
            Email=input("Enter your email:")
            Password=input("Enter your password:")
            if Email==data[self.email]:
                    if Password==data[self.password]:
                        print("You are login successfully..")
                        break    
                    else:
                        print("Sorry please enter valid credentials")
            else:
                print("Invalid credentials")
            break
        return data
    def Place_new_order(self):
        order_id=0
        order_id+1
        self.order_food_items=[]
        list_of_foods=[{"Name":"Tandoori chicken", "Quantity":" 4 Pieces", "Price":240}{"Name":"Vegan Burger", "Quantity":" 1 Pieces", "Price":320}{"Name":"Truffle Cake", "Quantity":" 500 gram", "Price":900}]
        print("Here is the menu..")
        for i in list_of_foods:
            print(i)
        user_input = int(input("Select the food items which you want to oredr:"))
        if user_input==0:
            self.self.order_food_tems.append(list_of_foods[0])
        elif user_input==1:
            self.self.order_food_tems.append(list_of_foods[1])
        elif user_input==2:
            self.self.order_food_tems.append(list_of_foods[2])
        else:
            print("Choose item from menu")
            print("Press 1 for order conformation:")
            print("Press 2 for oredr conformation:")
            option=int(input("Enter your choice:"))
            if option ==1:
                print("Order placed sucessfully")
            else:
                print("order cancelled")
        return self.order_food_items 
    def order_history(self):
        for i in self.order_food_items:
            print("order history is:" ,i)
    def Edit_profil(self):
        with open("personal_details.json","w")as f:
            data = json.load(f)
        for k, in data.items():
            print(f"user mail id:{k} || iser details:{v}")
        mail_id = input("Enter mail id which you want to updtae:")
        field=input("Enter field which you want to update:")
        updated_value = input("Enter updated value:")
        data[mail_id][field]=updated_value
        with open("personal_details.json","w")as f:
            json.dump(data,f,indent=4)
        return data


x =user()
print(x.Register())
print(x.Login())
print(x.Place_new_order())
print(x.order_history())
print(x.Edit_profil())