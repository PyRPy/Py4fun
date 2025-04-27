# one example of how to use decorator
# this example is adpated from chatgpt 
def my_decorator(func):
    def wrapper():
        print("this is before the function is called")
        func()
        print("this is after the function is called")
    return wrapper 

# use decorator defined above
@my_decorator
def say_hello():
    print("hello")

say_hello()

