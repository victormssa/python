for counter in range(10):
    print(counter, end= ',')
for number in range(5, 10):
    if number == 8:
        break
    print(number, end= ',')
for number in range(0, 10, 2):
    if number == 6:
        continue
    print(number, end= ',')