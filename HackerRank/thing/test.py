def fizzBuzz(n):
    # Write your code here

    for x in range(1, n):
        
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x %3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)



fizzBuzz(10)