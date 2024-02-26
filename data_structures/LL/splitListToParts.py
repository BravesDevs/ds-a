class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None


class Solution:

    def split_list(self, lst, k):
        ans = []
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        part, left = n//k, n % k
        cur = head
        prev = None
        for i in range(k):
            ans.append(cur)
            for _ in range(part):
                if cur:
                    prev = cur
                    cur = cur.next

            if left and cur:
                prev = cur
                cur = cur.next
                left -= 1

            if prev:
                prev.next = None

        return ans


sln = Solution()

n1 = ListNode(1)
n1.next = ListNode(2)
n1.next.next = ListNode(3)

print(sln.splitListToParts(n1, 5))
