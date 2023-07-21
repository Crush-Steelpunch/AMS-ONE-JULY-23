# def case(func, string):
#     return func(string)
# 
# print(case(str.upper, "hello world")) # Prints HELLO WORLD
# breakpoint()
# print(case(str.lower, "LOREM IPSUM")) # Prints lorem ipsum
def my_first_decorator(func):
    def wrapper(name):
        print("This is some new functionality!!")
        return func(name)

    return wrapper

def greet(name):
    return f"Hello, {name}!"

breakpoint()

greet = my_first_decorator(greet)

print(greet("Bob Smith"))