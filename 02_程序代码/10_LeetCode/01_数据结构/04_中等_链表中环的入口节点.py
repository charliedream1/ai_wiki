# -*- coding: utf-8 -*-
# @Author   : liyi
# @Time     : 2023/5/5 22:53
# @File     : 04_中等_链表中环的入口节点.py
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
题目：
 - 主站链接：https://leetcode-cn.com/problems/linked-list-cycle-ii/
 - 链接：https://leetcode.cn/problems/c32eOV/
难度：中等

================== 题目 ====================
给定一个链表，返回链表开始入环的第一个节点。 从链表的头节点开始沿着 next 指针进入环的第一个节点为环的入口节点。
如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，
则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
 

进阶：是否可以使用 O(1) 空间解决此题？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/c32eOV
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



================== 题解 ====================
方法一：哈希表
思路与算法

一个非常直观的思路是：我们遍历链表中的每个节点，并将它记录下来；一旦遇到了此前遍历过的节点，
就可以判定链表中存在环。借助哈希表可以很方便地实现。

作者：LeetCode-Solution
链接：https://leetcode.cn/problems/c32eOV/solution/lian-biao-zhong-huan-de-ru-kou-jie-dian-vvofe/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic = {}
        while head:
            if head in dic:
                return head
            dic[head] = True
            head = head.next
        return None
