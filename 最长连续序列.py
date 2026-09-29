class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        ans = 0
        for num in num_set:
            #如果num是连续序列的开始，才需要计算连续序列的长度
            if num - 1  in num_set:
                continue
            #计算连续序列的长度
            cur_len = 1
            current_num = num
            while current_num + 1 in num_set:
                current_num += 1
                cur_len += 1
            ans = max(ans,cur_len)

                
                
       



if __name__ == "__main__":
    s = Solution()
    nums = [100,4,200,1,3,2,1,2]
    print(s.longestConsecutive(nums))