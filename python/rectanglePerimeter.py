# https://www.codewars.com/kata/559a28007caad2ac4e000083
def perimeter(n):
    a = 0
    b = 1
    sum = 1
    for _ in range(n):
        a, b = b, a+b
        sum += b
    return sum * 4