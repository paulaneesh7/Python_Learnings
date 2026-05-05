def serve_chai():
    chai_type = "Masala"
    print(f"Chai type inside the function is {chai_type}")


chai_type = "Ginger"
serve_chai()
print(f"Chai type outside the function is {chai_type}")


def chai_counter():
    chai_order = "lemon" #Enclosing scope

    def print_order():
        chai_order = "Lemon"
        print(f"Chai order inner function is {chai_order}")
    print_order()
    print(f"Chai order outer function is {chai_order}")


chai_order = "Tulsi" #Global scope
chai_counter()
print(f"Chai order global scope is {chai_order}")


print("############################################################")

############################################################################

def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Masala"
        print(f"Chai type in kitchen is {chai_type}")
    kitchen()
    print(f"Chai type in update_order is {chai_type}")

update_order()


chai_type = "Ginger"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnain"
        print(f"Chai type in kitchen is {chai_type}")
    kitchen()

front_desk()
print(f"Chai type in global scope is {chai_type}")