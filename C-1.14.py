'''Python program to determine distinct pair of numbers in sequence whose value is odd'''
def odd_product(*data):
    a=set()
    for i in range(len(data)):
        if data[i]%2!=0:
            a.add(data[i])
    return True if(len(a)>1) else False
if __name__=='__main__':
    print(odd_product(1,3,3,4,3))