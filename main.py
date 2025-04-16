from typing import List

def twoSum(nums:List[int], target:int) -> List[int]:
    ans = list()
    for ind_i, i in enumerate(nums):
        for ind_j, j in enumerate(nums):
            if(i+j == target and ind_i != ind_j and ind_i < ind_j):
                ans.append(ind_i)
                ans.append(ind_j)
                return ans
    return
