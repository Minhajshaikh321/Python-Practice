# nums=[1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]
# def removeduplicate(nums):
#         i = 0
#         for j in range(1,len(nums)):
#             if nums[j] != nums[j-1]:
#                 nums[i] = nums[j-1]
#                 i += 1
#                 nums[i] = nums[-1]
#         return i+1
# nums=[1,1,2]
# removeduplicate(nums)

# nums=[1,1,2]
# 
def isValid(s):
        stack = []       
        mapping = {'(':')','[':']','{':'}'}
        for char in s:
            if char in mapping.keys():
                stack.append(mapping[char])
            elif not stack or stack[-1]!=char:
                print('stack not',stack[-1]!=char)

                return False
            else:
                stack.pop()
        return len(stack)==0
s = "(}"
isValid(s)        