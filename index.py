def calculate_sum(num):

    if num <= 1:
        return num
    
    return num + calculate_sum(num - 1)

print(calculate_sum(5))
