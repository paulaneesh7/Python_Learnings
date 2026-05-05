

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Green Tea"
    yield "Cup 3: Black Tea"


stall = serve_chai()

print(next(stall)) # Output: Cup 1: Masala Chai
print(next(stall)) # Output: Cup 2: Green Tea
print(next(stall)) # Output: Cup 3: Black Tea
# print(next(stall)) # Output: StopIteration error, as there are no more cups of chai to serve.