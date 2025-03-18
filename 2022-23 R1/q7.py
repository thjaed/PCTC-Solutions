total = 0

while True:
    a = int(input())

    if total + a < 20:
        total =+ a
    elif total + a > 20:
        total = 0
    elif total + a == 20:
        print(total)
        break