# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(self, head: Optional, n):
  """
  Args:
      head : Liked List Node
      n : Integer
  Returns:
      head: Returns a linked list with the nth element from the end removed
  """
  if not head: return head
  fast = slow = head
  for _ in range(n):
      fast = fast.next
  if not fast:
      return head.next
  while fast.next:
      slow = slow.next
      fast = fast.next
  slow.next = slow.next.next
  return head
