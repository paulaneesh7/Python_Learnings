# Given a list of numbers. write a program to turn every item of a list into its square.

def elements_square(lst):
    for i in range(len(lst)):
        l = []
        for i in range(len(lst)):
            l.append(lst[i]*lst[i])

        return l


print(elements_square([1,2,3,4]))