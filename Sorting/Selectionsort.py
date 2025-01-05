def selectionsort(array):
    for i in range(len(array)):
        min_index =i
        for j in range(i+1,len(array)):
            if array[min_index] < array[j]:
                min_index =j
                
        array[min_index],array[j] = array[j],array[min_index]
    
    return array
    
    
array = [10,50,20,30,30,25,915,75]

result = selectionsort(array)
print(result, end = '')