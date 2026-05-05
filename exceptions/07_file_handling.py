

# try: 
#     file = open("order.txt", "w")
#     file.write("Order: Masala Chai\n")
# finally:
#     file.close()    



with open("order.txt", "w") as file:
    file.write("Order: Ginger Chai\n")
