def oddeven(numbers):
    odd = []
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

print(oddeven([1, 2, 3, 4, 5, 6]))