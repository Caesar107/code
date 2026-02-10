# 234. 回文链表
# 已解答
# 简单
# 相关标签
# premium lock icon
# 相关企业
# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。

 

# 示例 1：


# 输入：head = [1,2,2,1]
# 输出：true
# 示例 2：


# 输入：head = [1,2]
# 输出：false
 

# 提示：

# 链表中节点数目在范围[1, 105] 内
# 0 <= Node.val <= 9
 

# 进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


#思路1：前进存列表 只存一半，遇到head=.next 里面开始比较两侧。
#问题是11233211这种 会直接去比较11


#思路2：存整个链表，然后中间开始比较：

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        lis=[]
        #h=head
        while head:
            lis.append(head.val)
            head=head.next
        half_l=len(lis) // 2

        if len(lis) %2 != 0:
            i=(len(lis)//2)-1
            j=(len(lis)//2)+1
        else:    
            i=(len(lis)//2)-1
            j=(len(lis)//2)

        for k in range(0,half_l):
            if lis[i] == lis[j]:
                i=i-1
                j=j+1
            else:
                return False
        return True


#简化
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # 1) 拉平到数组
        vals = []
        cur = head
        while cur:
            vals.append(cur.val)
            cur = cur.next

        n = len(vals)
        i = (n - 1) // 2      # 左指针（中点左侧）
        j = n // 2            # 右指针（偶数=mid，奇数=mid+1）

        # 2) 从中间向两侧比
        while i >= 0:  ###这里很关键 如果用什么那个for的判断 遇到100这样的就只会比较一次 0=0结束了
            if vals[i] != vals[j]:
                return False
            i -= 1
            j += 1
        return True
    


#方法3：快慢指针 + 反转链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        if fast:
            slow=slow.next


        rev = self.reverse(slow)

        p1, p2 = head, rev
        while p2:                     
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


    def reverse(self, Node):
        tool=None
        new=Node
        while new:
            next=new.next
            new.next=tool
            tool=new
            new=next
        return tool






