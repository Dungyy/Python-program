#!/usr/bin/python3

#SAMPLE INVENTORY PROGRAM

class Supply:
    def __init__(self, part, stock, shipped, process):
        if not part:
            raise ValueError("Missing Part Number")
        if stock < 100:
            print('Warning: Less then 100 Parts in stock\n')
        elif stock <= 50:
           print("WARNING RUNNING LOW")
        if process <= 50:
            print(f"Start Producing more of product\n")        
        self.part = part
        self.stock = stock
        self.shipped = shipped
        self.process = process

def main():
    inventory = get_product()
    print(f"Part #{inventory.part} has {inventory.shipped} parts shipped")
    print(f"{inventory.process} are being processed and we have {inventory.stock} parts in stock")


def get_product():
    part = int(input("Whats the Part Number: "))
    stock = int(input("In Stock: "))
    shipped = int(input("Shipped: "))
    process = int(input("In Progress: "))
    inventory = Supply(part, stock, shipped, process)
    return inventory


if __name__ == "__main__":
    main()