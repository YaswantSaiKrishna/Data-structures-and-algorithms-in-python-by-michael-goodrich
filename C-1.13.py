'''Python program to reverse list'''
def reverse_list(data):
    for i in range((len(data))-1,-1,-1):
        data.append(data[i])
        data.pop(i)
    print("2",data)
if __name__=='__main__':
    lis=[1,2,3,4,5]
    print("1:",*reversed(lis))
    reverse_list(lis)

