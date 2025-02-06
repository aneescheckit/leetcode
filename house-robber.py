class Solution:
    def rob(self, nums: List[int]) -> int:     
        currentMaxRob = [nums[0]]
        k = -1
        for i in range(1, len(nums)):
            if k == -1:
                if nums[i] > nums[i-1]:
                    currentMaxRob.append(nums[i])
                else:
                    currentMaxRob.append(nums[i-1])
            else:
                if nums[i] + currentMaxRob[k] > currentMaxRob[k+1]:
                    currentMaxRob.append(nums[i] + currentMaxRob[k])
                else:
                    currentMaxRob.append(currentMaxRob[k+1])
            k+=1
        
        return currentMaxRob[len(currentMaxRob)-1]