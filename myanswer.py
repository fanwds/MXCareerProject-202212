# 1
sum = 0
for x in range(100, 1000):
    first = x//100  # the first number
    second = (x//10)%10 # the second number
    third = x%10 # the third number
    sum = first**3 + second**3 + third**3
    if sum == x:
        print(x)

# 2
class Solution(object):
    def majorityElement(self, nums):
        maj_number = len(nums)//2
        num_dic = {}
        for num in nums:
            if num not in num_dic:
                num_dic[num] = 1
            else:
                num_dic[num] += 1
        
        for key, value in num_dic.items():
            if value > maj_number:
                return key

# 3
class Solution(object):
    def isValid(self, s):
        if len(s)%2 != 0:
            return False
        par_dict = {"(":")", "[":"]", "{":"}"}
        stack = []
        for label in s:
            if label in par_dict.keys():
                stack.append(label)
            else:
                if stack == []:
                    return False
                else:
                    open_par = stack.pop()
                    if label != par_dict[open_par]:
                        return False
        return stack == []






