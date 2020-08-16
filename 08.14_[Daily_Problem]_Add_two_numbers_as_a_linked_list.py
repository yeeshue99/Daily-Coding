# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    temp = {"dsa": 0, "dsasadsa": 10}

    def addTwoNumbers(self, l1, l2, c=0):
        val = l1.val + l2.val + c
        carry = 0
        if val >= 10:
            val %= 10
            carry = 1

        l3 = ListNode(val)
        if l1.next and l2.next:
            l3.next = Solution().addTwoNumbers(l1.next, l2.next, carry)
        elif l1.next:
            l3.next = Solution().addTwoNumbers(l1.next, ListNode(0), carry)
        elif l2.next:
            l3.next = Solution().addTwoNumbers(ListNode(0), l2.next, carry)
        elif c:
            l3.next = ListNode(c)

        return l3

    def addTwoNumbersIter(self, l1, l2):
        a = l1
        b = l2
        c = 0
        ret = current = None

        while a or b:
            val = a.val + b.val + c
            c = val // 10
            if not current:
                ret = current = ListNode(val % 10)
            else:
                current.next = ListNode(val % 10)
                current = current.next

            if a.next or b.next:
                if not a.next:
                    a.next = ListNode(0)
                if not b.next:
                    b.next = ListNode(0)
            elif c:
                current.next = ListNode(c)
            a = a.next
            b = b.next
        return ret


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(6)

result = Solution().addTwoNumbers(l1, l2)
while result:
    print(result.val)
    result = result.next

result = Solution().addTwoNumbersIter(l1, l2)
while result:
    print(result.val)
    result = result.next
# 7 0 0 1
