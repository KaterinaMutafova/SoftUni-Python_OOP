x = "global"

def outer():
    x = "local"

    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
        return x

    def change_global():
        global x
        x = "global: changed!"


    print("outer:", x)
    x = inner()
    print("outer:", x)
    change_global()

print(x)
outer()
print(x)
