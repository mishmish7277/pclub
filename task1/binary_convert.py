def convertToBinary(num,memory):
    arr = [0] * memory
    for i in range(len(arr)-1,0,-1):
        if num % 2 != 0:
            arr[i] = 1
            num = num // 2
        else:
            num = num // 2

    for i in range(0,len(arr)):
        arr[i] = 1 - arr[i]
        
    j = -1
    result = 2
    while (result == 2):
        result = arr[j] + 1
        if result == 1:
            arr[j] = 1
        else:
            arr[j] = 0
        j = j - 1
        
    print(arr)
   
             
            
             
convertToBinary(5,8)
                

    
