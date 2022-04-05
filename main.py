# задание 1

def nums_odd_gen(max_num):
    for num in range(1, max_num+1, 2):
        yield num
num_odd = nums_odd_gen(41)
# print(*num_odd)
print(next(num_odd))
print(next(num_odd))
print(next(num_odd))

# задание 2

max_num_2 = 33
nums_odd = [num for num in range(1, max_num_2 + 1, 2)]
print(nums_odd)