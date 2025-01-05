# def mydecorator(function):
    
#     # adding *args and **kwargs will make our decorator universal
#     def wrapper(*args,**kwargs):
#         print("I mam decorating your function")
#         function(*args,**kwargs)

#     return wrapper

# @mydecorator
# def hello_world():
#     print("Hello World!")

# hello_world()


# Pratical example

def logged(function):

    def wrapper(*args,**kwargs):
        value = function (*args, **kwargs)
        with open('logfile.txt', 'a+') as f:
            fname = function.__name__
            print(f"{fname} returned value {value}")
            f.write(f"{fname} returned value {value}\n")
        return value
    return wrapper

@logged
def add(x,y):
    return x+y

print(add(10,10))


# Pratical example 2

import time
def timed(function):
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        fname = function.__name__
        print(f"{fname} took {after-before} seconds to execute")
        return value

@timed
def myfunction(x):
    result=1
    for i in range(1,x):
        result *= i
