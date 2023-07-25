# -*- coding: utf-8 -*-
# @Author   : liyi
# @Time     : 2023/6/3 16:58
# @File     : 正负有序数组排序.py
# @Project  : ai_quant_trade
# Copyright (c) Personal 2022 liyi
# Function Description: 
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
题目
给已排序数组（有正有负）按照绝对值大小进行排序,给出尽可能最优的时间复杂度和空间复杂度
（绝对值相同的，正数排前面）

思路
数组大概是这样,{-20, -9, -4, -1, -1, 0, 3, 5, 19}

如果负数且有正数存在,那么绝对值最小的一定在中间,绝对值最大的一定在左右两侧。那么可以有两种思路

额外设置一个大小为n的数组（空间复杂度 O(n)）

先找到绝对值最小的（二分查找,时间复杂度O(log(n))）,分别向左右两边进行遍历、比较,按绝对值从小到大赋值到新数组(时间复杂度O(n)),
总时间复杂度为O(n)
设置l, r指针,从左右两端向里进行遍历、比较,按绝对值从大到小的顺序赋值到新数组（时间复杂度O(n)）。
"""


class Solution:
    def sort_abs(self, nums: list):
        if not len(nums):
            return None

        l, r = 0, len(nums) - 1
        p = len(nums) - 1
        ans = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) >= abs(nums[r]):
                ans[p] = nums[l]
                l += 1
            else:
                ans[p] = nums[r]
                r -= 1
            p -= 1
        return ans


def main():
    nums = [-20, -9, -4, -1, -1, 0, 3, 4, 5, 19]
    slu = Solution()
    ans = slu.sort_abs(nums)
    print('ori: ', nums)
    print('ans: ',  ans)


if __name__ == '__main__':
    main()
