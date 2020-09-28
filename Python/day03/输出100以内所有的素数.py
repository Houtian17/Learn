for i in range(2, 100):
    sum = 0
    for j in range(2, i + 1):
        if i % j == 0:
            sum = sum + 1

    if sum == 1:
        print(i)
