class Bikeshop:
    def __init__(self,stock):
        self.stock = stock

    def displayBike(self):
        print("Total Bikes",self.stock)

    def rentForBike(self,Quantity):
        if Quantity<=0:
            print("Enter positive number")
        elif Quantity>self.stock:
            print("Enter the value less than stock")
        else:
            self.stock= self.stock-Quantity
            print("Total price",Quantity*100)
            print("Total Bikes",self.stock)

while True:
    obj = Bikeshop(100)
    User_Choice = int(input('''
    1 Display Number of Bikes available
    2 Rent Bike
    3 Exit
    '''))
    if User_Choice ==1:
        obj.displayBike()
    elif User_Choice ==2:
        n = int(input("Enter the Quantity:--- "))
        obj.rentForBike(n)
    else:
        break