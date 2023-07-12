def good_pair(arr,pair):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(1,n):
            if i!=j:
                if arr[i]+arr[j]==pair:
                    count+=1
    if count>=1:
        return 1
    else:
        return 0
arr= list(map(int,input("Enter the array:").split()))
pair = int(input("Enter the value:"))
print(good_pair(arr,pair))
