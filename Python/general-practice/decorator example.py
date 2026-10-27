def loud (func):
    def wrapper (*arg, **kwarg):
       return func().upper()
    return wrapper

def low (func):
    def wrapper (*arg, **kwarg):
       return func().lower()
    return wrapper

@loud
def greeting ():
    return "Hello World !"

print (greeting())