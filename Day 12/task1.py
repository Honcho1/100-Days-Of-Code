# Check if a number is a prime number

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

# Test the function
number = int(input("Enter a number: "))
print(is_prime(number))