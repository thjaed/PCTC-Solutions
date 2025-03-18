a = int(input())
b = int(input())

add = 100 - (a + b)
sub_1 = 100 - (a - b)
sub_2 = 100 - (b - a)

if add < 0:
    add = add * -1

if sub_1 < 0:
    sub_1 = sub_1 * -1

if sub_2 < 0:
    sub_2 = sub_2 * -1
    

if add < sub_1 and add < sub_2:
    print(add)
elif sub_1 < add and sub_1 < sub_2:
    print(sub_1)
elif sub_2 < add and sub_2 < sub_1:
    print(sub_2)