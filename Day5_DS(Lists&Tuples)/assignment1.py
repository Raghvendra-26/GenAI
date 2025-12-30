
# min, max from a list 

def find_min_max(numbers):
    
    if len(numbers) == 0:
        return None,None
    min_value = numbers[0]
    max_value = numbers[0]
    
    for i in range(1,len(numbers)):
        if numbers[i] < min_value :
            min_value = numbers[i]
        
        if numbers[i] > max_value :
            max_value = numbers[i]
    
    return min_value,max_value
    
    
numbers = [5, 4, 7, 6, 3, 8, 2]
minimum, maximum = find_min_max(numbers)

print("Minimum number is:", minimum)
print("Maximum number is:", maximum)