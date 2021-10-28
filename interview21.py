def sumup(arr,k):
    dict1={}
    for i in range(len(arr)):
        if k-arr[i] not in dict1:
            dict1[arr[i]]=0
        else:
            return (arr[i],k-arr[i])
    return -1
arr=[1,5,2,3,7,10]
k=21
print(sumup(arr,k))