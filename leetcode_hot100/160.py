#相交链表
# 给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

# 图示两个链表在节点 c1 开始相交：



# 题目数据 保证 整个链式结构中不存在环。

# 注意，函数返回结果后，链表必须 保持其原始结构 。

# 自定义评测：

# 评测系统 的输入如下（你设计的程序 不适用 此输入）：

# intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
# listA - 第一个链表
# listB - 第二个链表
# skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
# skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
# 评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。

 

# 示例 1：



# 输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# 输出：Intersected at '8'
# 解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
# 在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
# — 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
 

# 示例 2：



# 输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
# 输出：Intersected at '2'
# 解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
# 从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
# 在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
# 示例 3：



# 输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
# 输出：No intersection
# 解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
# 由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
# 这两个链表不相交，因此返回 null 。
 

# 提示：

# listA 中节点数目为 m
# listB 中节点数目为 n
# 1 <= m, n <= 3 * 104
# 1 <= Node.val <= 105
# 0 <= skipA <= m
# 0 <= skipB <= n
# 如果 listA 和 listB 没有交点，intersectVal 为 0
# 如果 listA 和 listB 有交点，intersectVal == listA[skipA] == listB[skipB]
 

# 进阶：你能否设计一个时间复杂度 O(m + n) 、仅用 O(1) 内存的解决方案？

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def get_length(self,head):
        len=0
        while head:
            len+=1
            head=head.next
        return len

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_A=self.get_length(headA)
        len_B=self.get_length(headB)
        if len_A>len_B:
            for _ in range(len_A-len_B):
                headA=headA.next
        else:
            for _ in range(len_B-len_A):
                headB=headB.next

        while headA and headB:
            if headA == headB:
                return headA
            headA =headA.next
            headB=headB.next
        return None
            
            

#换头法：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A=headA
        B=headB 
        while A is not B:
            if A:
                A=A.next
            else:
                A=headB 
            if B:
                B=B.next
            else:
                B=headA
        return A

# ACM/竞赛模式：从标准输入读取，手动构造链表并求交点

import sys

class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

class Solution:
    def getIntersectionNode(self, headA, headB):
        pA, pB = headA, headB
        while pA is not pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA  # 可能是交点节点，也可能是 None

def build_list(arr):
    """由数组构造单链表，返回头节点与数组对应的所有节点列表（便于按索引取节点）"""
    dummy = ListNode(0)
    cur = dummy
    nodes = []
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
        nodes.append(cur)
    return dummy.next, nodes

def main():
    data = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            data.append(line)
    # 期望 5 行输入
    if len(data) < 5:
        print("null")
        return

    intersectVal = int(data[0])
    m, n = map(int, data[1].split())
    listA = list(map(int, data[2].split()))
    listB = list(map(int, data[3].split()))
    skipA, skipB = map(int, data[4].split())

    # 构造两条链表
    headA, nodesA = build_list(listA)
    headB, nodesB = build_list(listB)

    # 根据 intersectVal/skipA/skipB 建立“相交”
    # 与 LeetCode 自定义评测一致：如果 intersectVal != 0，
    # 让 B 的第 skipB 个节点.next 指向 A 的第 skipA 个节点（两者应当值相等）
    if intersectVal != 0:
        # 安全检查：索引合法且值匹配（不匹配也照样连，值仅用于人类校验）
        if 0 <= skipA < len(nodesA) and 0 <= skipB < len(nodesB):
            nodesB[skipB].next = nodesA[skipA]

    # 调用算法
    inter = Solution().getIntersectionNode(headA, headB)
    if inter:
        print(inter.val)
    else:
        print("null")

if __name__ == "__main__":
    main()

            


        
        
        
        