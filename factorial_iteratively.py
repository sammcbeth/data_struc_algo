def factorial(num):
    answer = 1
    while num > 1:
        answer = answer * num
        num -= 1
    return answer


print(factorial(4))
