def areElementsContiguous(arr, n): 

    # Sort the array 

    arr.sort() 

      

    # After sorting, check if  

    # current element is either 

    # same as previous or is  

    # one more. 

    for i in range(1,n): 

        if (arr[i] - arr[i-1] > 1) : 

            return 0

    return 1

  
# ever after

arr = [ 5, 2, 3, 6, 4, 4, 6, 6 ] 

n = len(arr) 

if areElementsContiguous(arr, n): print("Yes") 

else: print("No") 
