'''Sum of squares of a positive integer n'''
def sum_of_square(n):
    return sum((i*i) for i in range(n) if (n>0))
if __name__=='__main__':
    print(sum_of_square(5))