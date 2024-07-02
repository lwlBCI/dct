def add_numbers(x,y):
    print(f"adding {x} to {y}")

    result = x+y

    print(f"result:{result}")

    return result
def main(x0,y0):
    x1 = x0 * 3
    y1 = y0 * 4

    return add_numbers(x1,y1)

a=5
b=6
c=main(a,b)
f = 'hello'