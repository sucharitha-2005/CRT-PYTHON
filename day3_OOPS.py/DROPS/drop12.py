class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display_specs(self):
        print("Laptop Specifications:")
        print(f"Brand: {self.brand}")
        print(f"RAM: {self.ram}")
        print(f"Storage: {self.storage}")


