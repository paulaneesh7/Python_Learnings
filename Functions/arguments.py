

def make_chao(tea, milk, sugar):
    print(f"Making chao with {tea}, {milk}, and {sugar}.")


make_chao("green tea", "almond milk", "honey")
make_chao(tea="black tea", milk="cow milk", sugar="sugar")

# def func(*args, **kwards): *args -> arguments as tuple, **kwards -> keyword arguments as dictionary
def special_chai(*ingredients, **extras):
    print("Ingredients ", ingredients)
    print("Extras ", extras)


special_chai("Cinnamon", "Cardmon", "honey", sweetener="stevia", foam="yes")