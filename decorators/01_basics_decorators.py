

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper


@my_decorator
def greet():
    print("Hello from decorators class from TechnoHub!")


greet()

# Before function runs
# Hello from decorators class from TechnoHub!
# After function runs


print(greet.__name__) # output is: greet but without using the imported @wraps output will be: wrapper