class Product_Conversion:
    def __init__(self, id, name, description, price, inventory_quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.inventory_quantity = inventory_quantity

    @staticmethod
    def product_decoder(product):
        return Product_Conversion(product["id"], product["name"], product["description"], product["price"], product["inventory_quatity"])
    
    @staticmethod
    def product_encoder(obj):
        pass