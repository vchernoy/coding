
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def listLen(self, l):
        size = 0
        while l is not None:
            size += 1
            l = l.next
        
        return size
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = self.listLen(l1)
        len2 = self.listLen(l2)
        resLen = max(len1, len2) + 1
        i1 = 0
        i2 = 0
        cur1 = l1
        cur2 = l2
        head = ListNode(0)
        cur = head
        while cur1 is not None:
            if len1 - i1 > len2 - i2:
                n = ListNode(cur1.val)
                cur1 = cur1.next
                i1 += 1
            elif len1 - i1 < len2 - i2: 
                n = ListNode(cur2.val)
                cur2 = cur2.next
                i2 += 1
            else:
                n = ListNode(cur1.val + cur2.val)
                cur1 = cur1.next
                cur2 = cur2.next
                i1 += 1
                i2 += 1
            
            cur.next = n
            cur = n

        # funny -- how to solve the carry problem
        while True:
            carry = False
            cur = head
            while cur.next is not None:
                nextDigit = cur.next.val
                if nextDigit >= 10:
                    cur.val += nextDigit / 10
                    cur.next.val = nextDigit % 10
                    carry = True

                cur = cur.next

            if not carry: 
                break # no carry found, so we can leave the loop           
             
        while (head.next is not None) and (head.val == 0):
            head = head.next
             
        return head

