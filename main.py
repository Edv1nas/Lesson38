"""Create a dataclass named "Product" that has the following attributes: product_id: int name: str price: float quantity: int 
The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity. 
Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost. 
Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost."""

from typing import List
from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self) -> int:
        return self.price * self.quantity
    
def find_highest_product_cost(products: List[Product]) -> Product:
    highest_cost = 0
    # highest_cost_product = None
    for product in products:
        total_cost = product.total_cost()
        if total_cost > highest_cost:
            highest_cost = total_cost
            highest_cost_product = product.name
    return highest_cost_product

product_list = [
    Product(1, "Pienas", 1.5, 13),
    Product(2, "Kefyras", 1.2, 11),
    Product(3, "Sūris", 4.99, 10),
    Product(4, "Sviestas", 2.99, 5),
    Product(5, "Varškė", 2, 22),
]

while True:
    print("\n")
    print("1. Print all product in list")
    print("2. Show product with highest cost")
    print("3. Quit")

    choice = int(input("Enter your choice (1-3): "))
    if choice == 1:
        for product in product_list:
            print(f"Product id: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    elif choice == 2:
        highest_product_cost = find_highest_product_cost(product_list)
        print(f"Product highest total cost: {find_highest_product_cost(product_list)}")


    elif choice == 3:
        break
