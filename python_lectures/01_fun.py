def is_prime(num):
    for n in range(2,num):
        if num%n == 0:
            print("number is not prime")
            break
    else:
            print("number is prime")
is_prime(23)
            