array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(1, len(array)):
    if array[i] % i:
        print(i)
