'''Python program to find minmax using built-in functions'''
def minmax(*data):
    return (*data,*data) if len(data)==1 else (min(data),max(data))
if __name__=='__main__':
    print(minmax(4,100,10,1))