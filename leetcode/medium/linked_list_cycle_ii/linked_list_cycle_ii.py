
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = self.cycle([head, head], [1,2])
        if h == head:
            return h
        return self.cycle([head, h], [1,1])

    def cycle(self, heads, incs):
        while True:
            for i in range(2):
                h = heads[i]
                for _ in range(incs[i]):
                    if h is None:
                        return None
                    h = h.next
                heads[i] = h

            if heads[0] == heads[1]:
                return heads[0]

