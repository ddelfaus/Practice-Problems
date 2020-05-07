def fibonacci(n):

    #base case
    if n < 1:
        return n
    
    
    else:
      
        return fibonacci(n - 1) + fibonacci(n-2)

print(fibonacci(3))



memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]