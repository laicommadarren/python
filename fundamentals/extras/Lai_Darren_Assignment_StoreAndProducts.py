class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)

    def sell_product(self, id):
        print(f"Item sold: {self.products[id]}")
        self.products.pop(id)

    # def inflation(self, percent_increase):
        # for index in self.products:
            # self.products[index].update_price(percent_increase, True)


class Product:
    def __init__(self, product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category

    def print_info(self):
        print(f"Product: {self.product_name}, Category: {self.category}, Price: {self.price}")
        return self
    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price *= (1 + percent_change)
        else:
            self.price *= (1 - percent_change)

test_store = Store("Darren's store")
pineapple_product = Product("pineapple", 5, "fruit")
chips_product = Product("chips", 3, "snacks")
test_store.add_product(pineapple_product)
test_store.add_product(chips_product)
pineapple_product.print_info()
chips_product.print_info()
pineapple_product.update_price(.2, True)
pineapple_product.print_info()
test_store.sell_product(1)
