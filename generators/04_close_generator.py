

def local_menu():
    yield "Chai"
    yield "Samosa"
    yield "Kachori"
    yield "Pav Bhaji"


def imported_chai():
    yield "Masala Chai"
    yield "Green Tea"
    yield "Black Tea"



def full_menu():
    yield from local_menu()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Welcome! What would you like to order?"
            print(f"Preparing your {order}...")
    except:
        print("Stall closed, No more chai")



stall = chai_stall()

print(next(stall))

# always close your generators when you are done with them
stall.close()


# Generators in 5-6 steps
# 1. yield
# 2. next()
# 3. send()
# 4. yield from
# 5. close()