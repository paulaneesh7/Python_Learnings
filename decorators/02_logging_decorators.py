from functools import wraps



def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"✅ Function '{func.__name__}' returned: {result}")
        return result
    return wrapper



@log_activity
def brew_chai(type, milk=True, sugar=True):
    print(f"Brewing a cup of {type} chai... and adding {'milk' if milk else 'no milk'} and {'sugar' if sugar else 'no sugar'}")


brew_chai("Masala")