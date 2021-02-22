def rhombus(n):
    for i in range(n):
        offset = (n - i - 1) * ' '
        content = "* " * (i + 1)
        print(f"{offset}{content}")
    for i in range(n - 2, -1, -1):
        offset = (n - i - 1) * ' '
        content = "* " * (i + 1)
        print(f"{offset}{content}")


rhombus(3)