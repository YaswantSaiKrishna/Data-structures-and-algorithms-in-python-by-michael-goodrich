'''Python code to find sum of odd positive integers'''
def sum_of_squares_of_odd_positive_integers(n):
    return sum((i*i) for i in range(1,n,2) if(n>=0))
if __name__=='__main__':
    print(sum_of_squares_of_odd_positive_integers(5))