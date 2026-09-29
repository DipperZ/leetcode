# 练习：在独立分支上完善螺旋矩阵
from typing import List

class solution():
    def generate_matrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        #循环次数
        loop = n//2     
        #当前循环次数
        cur_loop = 0            
        #当前循环的起始点
        start = cur_loop
        end = n - cur_loop - 1
        #当前循环的数字
        num = 1 



        
        
     
        