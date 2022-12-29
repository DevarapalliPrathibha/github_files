class shoppinglist:
    dict = {"vivo":1000,"oppo":20000,"iphone":50000,"nokia":30000}
    cart = {}
    def update_shoppinglist(self,item,value):
        self.dict[item] = value
        print(self.dict)
    def update_cart(self,item,quantity):
        self.cart[item] = quantity
    def display_cart(self):
        for key,values in self.cart.items():
            print(key,values)
    def delete_cart(self,item):
        del self.cart[item]
    def total(self):
        for self.item in self.dict:
            if self.item in self.cart:
                count = self.dict[self.item]*self.cart[self.item]
                print(count)



shoplistObj = shoppinglist()
shoplistObj.update_shoppinglist("realme",22000)
shoplistObj.update_cart("vivo",3)
shoplistObj.update_cart("nokia",1)
shoplistObj.display_cart()
shoplistObj.delete_cart("vivo")
shoplistObj.display_cart()
shoplistObj.total()



