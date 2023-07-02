# coding: utf-8
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
        def get_number(s, type):
            if not s or s is None:
                return 0
            string_result = ""
            while s:
                string_result += str(s.val)
                s = s.next
            if type == "int":
                return int(string_result[::-1])
            if type == "str":
                return string_result[::-1]

        l1_int = get_number(l1, "int")
        l2_int = get_number(l2, "int")
        l1_l2_add_reverse = str(l1_int+l2_int)[::-1]

        dummy = ListNode(0)
        cur = dummy
        for i in range(len(l1_l2_add_reverse)):
            cur.next = ListNode(l1_l2_add_reverse[i])
            cur = cur.next
        return dummy.next


if __name__ == '__main__':
    """
    Example 1:
    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    """
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    print("l1 is {}, l2 is {}".format(l1, l2))

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    return_result = []
    while result:
        return_result.append(int(result.val))
        result = result.next

    print("最后输出结果是：{}".format(return_result))



