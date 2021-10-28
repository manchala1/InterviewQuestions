def sumup(arr,K):
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)-1):
            if(arr[i]+arr[j] == K):
                return arr[i],arr[j]
arr=[1,5,2,3,7,10]
k=9
print(sumup(arr,k))