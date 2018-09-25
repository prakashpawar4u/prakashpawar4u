foo = 100

def hello():
    print("I am from my_module ")


if __name__ == "__main__":
    print("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello()
