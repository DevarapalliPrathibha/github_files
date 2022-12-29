class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
    def display_Product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.rating)
class Electronic(Product):
    def __init__(self,warrenty):
        self.warrenty = warrenty

    def get_warrenty(self):
        print(self.warrenty)

class grocery(Product):
    def __init__(self,package,expirey_date):
        self.package = package
        self.expirey_date = expirey_date
    def get_expiry_date(self):
        print(self.expirey_date)
        pass
class order(Product):
    def __init__(self, order_type, order_address):
        items = {}
        self.order_type = order_type
        self.order_address = order_address
    def get_order_type(self):
        print(self.order_type)
    def get_order_address(self):
        print(self.order_address)

obj = Product("iphone","20000","18000","9.0")
obj.display_Product_details()
obj1 = Electronic(2)
obj1.get_warrenty()
obj2 = grocery("6-9-2001","9-4-2021")
obj2.get_expiry_date()
obj3 = order("package","tpt")
obj3.get_order_type()
obj3.get_order_address()
print("*****************************")
#using super
class Product:
    def __init__(self,name,price,deal_price,rating):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.rating = rating
    def display_Product_details(self):
        print(self.name)
        print(self.price)
        print(self.deal_price)
        print(self.rating)
class Electronic(Product):
    def __init__(self,warrenty):
        self.warrenty = warrenty

    def get_warrenty(self):
        print(self.warrenty)

class grocery(Product):
    def __init__(self,name,price,deal_price,rating,package,expirey_date):
        super().__init__(name,price,deal_price,rating)
        self.package = package
        self.expirey_date = expirey_date
    def get_expiry_date(self):
        print(self.expirey_date)
        pass
obj = Product("iphone","20000","18000","9.0")
obj.display_Product_details()
obj1 = Electronic(2)
obj1.get_warrenty()
obj2 = grocery("butter_milk",10,9,10,2001,2022)
obj2.get_expiry_date()