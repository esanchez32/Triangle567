def classify_triangle():

    # require that the input values be >= 0 and <= 200
    # call for user input for the three triangle lengths

    print('Enter sides of a triangle')

    print('Enter the length for triangle side a, a number >= 0 or <= 200')
    a = int(input('a = '))

    print('Enter the length for triangle side b, a number >= 0 or <= 200')
    b = int(input('b = '))

    print('Enter the length for triangle side c, a number >= 0 or <= 200')
    c = int(input('c = '))

    if a > 200 or b > 200 or c > 200:
        print('InvalidInput')
        
    elif a <= 0 or b <= 0 or c <= 0:
        print('InvalidInput')
    
    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle

    elif (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        print('NotATriangle')
        
    # now we know that we have a valid triangle 
    elif a == b == c:
        print('Equilateral')
    elif ((a ^ 2) + (b ^ 2)) == (c ^ 2):
        print('Right')
    elif (a != b) and (b != c) and (a != c):
        print('Scalene')
    else:
        return 'Isosceles'

