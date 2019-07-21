'''Python code to find weather a number n is a multiple of another number m '''
def is_multiple(n,m):
    return True if ((n//m)*m==n) else False
if __name__=='__main__':
    print(is_multiple(33,4))
