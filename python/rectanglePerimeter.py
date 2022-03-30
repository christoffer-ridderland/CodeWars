# https://www.codewars.com/kata/559a28007caad2ac4e000083
def perimeter(n):
    a = 0
    b = 1
    sum = 0
    for _ in range(n):
        a, b = b, a+b
        sum += 4 * b
    return sum + 4 # does not count first square