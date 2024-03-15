def chunking_by(numbers, chunck):
    list = [] #create an empty list to check the numbers
    if numbers: 
        for i in range(0, len(numbers), chunck): # Chunking Loop
            list.append(numbers[i:i+chunck]) 
        return list
    # Make an if condition; if it is not a number, it will return nothing.
    elif not numbers: 
        return []
    
print(chunking_by([5, 4, 7, 3, 4, 5, 4], 3))  
print(chunking_by([3, 4, 5], 1))
