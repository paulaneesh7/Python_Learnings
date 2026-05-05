

# Generators are used to create iterators, but with a different approach. 
# Generators are simple functions which return an iterable set of items, one at a time, in a special way


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i



for num in even_generator(10):
    print(num)