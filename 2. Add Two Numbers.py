# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = ListNode()

    def addTwoNumbers(self, l1, l2):
        current = self.head
        carry = 0
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0
            n = n1+n2+carry
            temp = n%10
            carry = n//10
            current.next = ListNode(temp)
            current = current.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return self.head.next