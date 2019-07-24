'''Count no of times a number must be divided to get a value less than 2'''
def posint(n):
    count=0
    while(n/2>2):
        n=n/2
        count+=1
    print(count+1)
if __name__=='__main__':
    posint(10)