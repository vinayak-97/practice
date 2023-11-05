class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums: return []

        res = []

        def backtrack(start, cur_lst):
            res.append(cur_lst[:])

            for i in range(start, len(nums)):
                cur_lst.append(nums[i])
                backtrack(i+1, cur_lst)
                cur_lst.pop()


        backtrack(0,[])

        return res
