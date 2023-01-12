def printChar(arr, Len):
 
    occ = {}
    for i in range(Len):
         
        if(arr[i] in occ):
            occ[arr[i]] = occ[arr[i]] + 1
         
        else:
            occ[arr[i]] = 1
  
    size = len(occ)
  
    while (size > 0):
  
        
        currentMax = 0
        arg_max = 0
        for key, value in occ.items():
 
            if (value > currentMax or (value == currentMax and key > arg_max)):
                arg_max = key
                currentMax = value
  
      
        print(f"{arg_max} - {currentMax}")
  
        occ.pop(arg_max)
        size -= 1
 
Str = "Mississippi"
Len = len(Str)
 
 
printChar(list(Str), Len)
 
