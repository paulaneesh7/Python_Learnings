

def chai_customer():
    print("Welcome! What chai would you like ?")
    order = yield
    while True:
        print(f"Preparing your {order}...")
        order = yield f"Your {order} is ready! Would you like to order another chai?"


customer = chai_customer()
next(customer)

customer.send("Masala Chai")
customer.send("Green Tea")
customer.send("Black Tea")