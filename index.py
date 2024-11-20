def calculate_sum(num):

    if num <= 1:
        return num
    
    return num + calculate_sum(num - 1)

n = int(input("Please enter a number: "))

sum = calculate_sum(n)

print(f"the sum from 1 to {n} is: {sum}")