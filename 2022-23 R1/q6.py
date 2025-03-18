initial_inv = int(input())
last_inv = initial_inv

while True:
    current_inv = int(input())
    if current_inv < last_inv:
        break
    else:
        last_inv = current_inv

print(current_inv - initial_inv)