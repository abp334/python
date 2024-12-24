class Pizza:
    size = ("small", "medium", "large")
    toppings = ("corn","tomato","onion","capsicum","mushroom","olives","broccoli")
    cheese = ("mozzarella", "feta", "cheddar")
    l = (50,100,200)
    def __init__(self,usersize,usertoppings,usercheese):
        self.size = usersize
        self.toppings = usertoppings
        self.cheese = usercheese
        self.prices = 0
    def price(self):
        self.prices += Pizza.l[Pizza.size.index(self.size)]
        for i in self.toppings:
            if i in ["brocolli","olives","mushroom"]:
                self.prices += 50
            elif i in ["capsicum","onion","tomato","corn"]:
                self.prices += 20
        for i in self.cheese:
            if i in Pizza.cheese:
                self.prices += 50
        return self.prices
class Order:
    def __init__(self,name,cid):
        self.name = name
        self.cid = cid
        self.orders = []
        self.bills = 0
    def order(self):
        size = input("Enter your choice of size(small/medium/large): ")
        n = int(input("Enter no of toppings you want: "))
        usertoppings = []
        for i in range(n):
            usertoppings.append(input("Enter toppings from corn/tomato/onion/capsicum/mushroom/olives/broccoli: "))
        n1 = int(input("Enter no of cheesse you want: "))
        usercheese= []
        for j in range(n1):
            usercheese.append(input("Enter your choice of cheese from mozzarella/feta/cheddar: "))
        self.orders.append(Pizza(size,usertoppings,usercheese))
    def bill(self):
        for i in self.orders:
            self.bills += i.price()
        return self.bills
name = input("Enter your name: ")
cid = input("Enter your id: ")
o = Order(name,cid)
while True:
    entry = int(input("Press 1 to order pizza, Press 2 to get bill and Press 3 to exit: "))
    if entry == 1:
        o.order()
    elif entry == 2:
        print(o.bill())
    elif entry == 3:
        exit()
#sir solution
#  class Pizza:
#     def __init__(self, size, toppings, cheese):
#         self.size = size
#         self.toppings = toppings
#         self.cheese = cheese
        
#     def price(self):
#         self.cost = 0
#         if self.size == 'small':
#             self.cost += 50
#         elif self.size == 'medium':
#             self.cost += 100
#         else:
#             self.cost += 200
#         topping_prices_20 = ['corn', 'tomato', 'onion', 'capsicum']
#         topping_prices_50 = ['mushroom', 'olives', 'broccoli']
#         for topping in self.toppings:
#             if topping in topping_prices_20:
#                 self.cost += 20
#             else:
#                 self.cost += 50
#         #for cheese
#         self.cost += 50 * len(self.cheese)
#         return self.cost
#     class Order:
#     def __init__(self, name, customerid):
#         self.name = name
#         self.customerid = customerid
 
#     def order(self, n):
#         self.pizzas = [] 
#         for i in range(n):
#             toppings = []
#             cheese = []
#             print('Customize Pizza',i+1)
#             size = input('Select size: ')
#             t = int(input('How many toppings: '))
#             for i in range(t):
#                 toppings.append(input('Enter toppings: '))
#             t = int(input('How many cheese: '))
#             for i in range(t):
#                 cheese.append(input('Enter cheese: '))
#             self.pizzas.append(Pizza(size, toppings, cheese))
 
#     def bill(self):
#         self.total = 0
#         count = 1
#         for p in self.pizzas:
#             print('Pizza', count)
#             print("Size:",p.size)
#             print("Toppings:",p.toppings)
#             print("Cheese:",p.cheese)
#             self.total += p.price()
#             count += 1
#         print('Total bill amount:', self.total)
# number=int(input("How many pizzas you want to order: "))
# order1 = Order('ABCD', 1)
# order1.order(number)
# order1.bill()
