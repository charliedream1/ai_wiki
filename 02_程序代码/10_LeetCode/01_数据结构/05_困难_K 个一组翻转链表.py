# -*- coding: utf-8 -*-
# @Author   : liyi
# @Time     : 2023/5/5 23:06
# @File     : 05_困难_K 个一组翻转链表.py
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


from typeguard import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stk = []
        cnt = 0
        p = ListNode(0)
        dummy = p
        while head:
            while cnt >= k:
                node = stk.pop()
                p.next = node
                p = node
                if not len(stk):
                    cnt = 0
            stk.append(head)
            head = head.next
            cnt += 1

        if len(stk) == k:
            while cnt >= k:
                node = stk.pop()
                p.next = node
                p = node
                if not len(stk):
                    cnt = 0
                    p.next = None
        elif len(stk) < k:
            p.next = stk[0]
        else:
            p.next = None

        return dummy.next
