# coding:utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        cur = dummy

        jinwei = 0
        mowei = 0

        while l1 and l2:
            add_int = l1.val + l2.val + jinwei
            jinwei = 0
            mowei = add_int
            if add_int >= 10:
                jinwei = add_int // 10
                add_int = add_int - jinwei * 10
            cur.next = ListNode(add_int)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            add_int = l1.val + jinwei
            jinwei = 0
            mowei = add_int
            if add_int >= 10:
                jinwei = add_int // 10
                add_int = add_int - jinwei * 10
            cur.next = ListNode(add_int)
            cur = cur.next
            l1 = l1.next

        while l2:
            add_int = l2.val + jinwei
            jinwei = 0
            mowei = add_int
            if add_int >= 10:
                jinwei = add_int // 10
                add_int = add_int - jinwei * 10
            cur.next = ListNode(add_int)
            cur = cur.next
            l2 = l2.next

        if jinwei > 0 and mowei >= 10:
            cur.next = ListNode(jinwei)

        return dummy.next


if __name__ == '__main__':
    """
    input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    output: [8,9,9,9,0,0,0,1]
    """

    l1 = ListNode(9)
    l1.next = ListNode(9)
    l1.next.next = ListNode(9)
    l1.next.next.next = ListNode(9)
    l1.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next = ListNode(9)
    l1.next.next.next.next.next.next = ListNode(9)

    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    l2.next.next.next = ListNode(9)

    print("l1 is {}, l2 is {}".format(l1, l2))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)
    return_result = []
    while result:
        return_result.append(result.val)
        result = result.next

    print("最后输出结果是：{}".format(return_result))



