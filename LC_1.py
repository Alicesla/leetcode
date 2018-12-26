def twoSum(self, nums, target):
        """
        self为空数组（自己添加）
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    self.append(i)
                    self.append(j)
                    return self
nums=[2,7,11,15,1,8]
target=9
self=[]
self=twoSum(self, nums, target)
print(self)
