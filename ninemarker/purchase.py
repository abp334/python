# write a class called product which should have product name,price,stock there should be a method to get a price
# that recieves number of item to buy and return cost of buying that item where the regular price is charged for order of less than
# 10 items, 10% discount is applied for order betwen 10 to 99 items and 20% discount is applied for order of more than 
# 100 items there should also be a method called make_purchase that recieve number of item to be bought and decrease from the
# stock
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
    def get_price(self,n):
        if n <= 10:
            return n * self.price
        if n > 10 and n <= 99:
            return n * self.price * 0.9
        if n > 100:
            return n * self.price * 0.8
    def make_purchase(self):
        n = int(input("Enter number of products you want to purchase: "))
        if n>0 and self.stock >n:
            self.stock -= n
            print(n,self.name,"purchased for ₹",self.get_price(n))
            print("Stock of",self.name,"left:",self.stock)
        else:
            print("input error or stock is empty")
name = input("Enter Product name: ")
price = int(input("Enter Product price: "))
stock = int(input("Enter Product stock: "))
p = Product(name,price,stock)
p.make_purchase()
