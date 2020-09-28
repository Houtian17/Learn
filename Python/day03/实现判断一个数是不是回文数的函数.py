def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10

    return total == num


if __name__ == '__main__':
    a = is_palindrome(121)
    print(a)
