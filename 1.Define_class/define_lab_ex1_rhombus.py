def draw_line(count_symbol, symbol, offset_count=0):
    offset = offset_count * ' '
    content = (f"{symbol} " * count_symbol).strip()
    return f"{offset}{content}"


def rhombus(n):
    for i in range(n):
        print(draw_line(i + 1, "*", n - i - 1))
    for i in range(n - 2, -1, -1):
        print(draw_line(i + 1, "*", n - i - 1))


n = int(input())
rhombus(n)


