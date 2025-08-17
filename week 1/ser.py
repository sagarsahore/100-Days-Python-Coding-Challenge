#write a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

    #test the function
print(factorial(5))  # Output: 120
#write a function for calculating the nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

        #Write a function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

#Write a function to find the maximum element in a list
def find_maximum(lst):
    if not lst:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element
 #Write a function to find the minimum element in a list
def find_minimum(lst):
    if not lst:
        return None
    min_element = lst[0]
    for num in lst:
        if num < min_element:
            min_element = num
    return min_element

