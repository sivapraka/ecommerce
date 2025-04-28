from datetime import time, datetime


def decorator(func):
    def wrapper(*args,**kwargs):
        print("Before executing the function")
        func(*args,**kwargs)
        print("After executing the function")
    return wrapper


def timeexecution(func):
    def wrapper(*args,**kwargs):
        start=datetime.now()
        print(start)
        func(*args,**kwargs)
    return wrapper

@timeexecution
@decorator
def display():
    print("Display function is called")


if __name__=="__main__":
    display()