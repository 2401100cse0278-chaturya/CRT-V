'''
Input : nums =[1,2,3,4]
Output :[1,3,6,10]
'''
nums=[1,2,3,4]
n=len(nums)
res=[0]*n
for i in range(n):
    s=0
    for j in range(n):
        s+=nums[j]
    res[i]=s
print(res)