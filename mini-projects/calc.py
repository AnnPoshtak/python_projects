nums = [2,10,5,6]
die = ["+","-","*"]
result = []
for i in range(len(nums)):
    while len(die) != len(nums):
        die.append("")
    result.append(nums[i])
    result.append(die[i])
print(eval("".join(map(str, result))))