def composed(f, g):
    def inner(x):
        return f(g(x))
    return inner

# Example usage:
def add_one(x):
    return x + 1

def square(x):
    return x * x

add_one_then_square = composed(square, add_one)

# Now, add_one_then_square behaves as square(add_one(x))
# print(add_one_then_square(5))  

def repeat(f, n):
    def inner(x):
        if(n == 1):
            return composed(f,lambda t : t)(x)
        repeat(f, n - 1)
    return inner
        
print(repeat(square, 2)(6))