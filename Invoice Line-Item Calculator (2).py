print()
print("The Invoice Line Item Calculator!")
print()
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")
price = get_price() 
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")
quantity = get_quantity()
print()

price = get_price()
quantity = get_quantity()
total = price * quantity
print(f"TOTAL:       {total}")
print()
    
def main():
    while True:
        price = get_price()
        quantity = get_quantity()
        print()

        while True:
            again = input("Enter another line item? (y/n): ")
            if again == 'y':
                break
            elif again == 'n':
                print()
                print("BYE!")    
                print("Press any key to continue . . .") 
                return
main()                                                                                         