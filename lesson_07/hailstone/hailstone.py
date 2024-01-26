
"""if num is ODD: *3 + 1
    if num is EVEN: /2 """

def hailstone (num1):
    while num1 != 1:
        print(num1)
        even_odd = num1 % 2
        if even_odd == 1:
            num1 = num1*3 + 1
        elif even_odd == 0:
            num1 = num1 / 2
    if num1 == 1:
        print(num1)
print(hailstone(3))