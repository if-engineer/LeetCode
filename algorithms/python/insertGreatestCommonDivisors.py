# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
  """
  Args:
      head: List Node

  Returns:
      Optional: Return Linked list with maximum common divisor added
  """
  while node.next:
      node.next = ListNode(gcd(node.val, node.next.val), node.next)
      node = node.next.next
  return head
