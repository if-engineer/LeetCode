# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
      """
      Args:
          head : LinkedList

      Returns:
        LinkedList: Reverse head node
      """
      if not head:
            return head
      prev_node, current_node = head, head.next
      prev_node.next = None
      while current_node:
          next_node = current_node.next
          current_node.next = prev_node
          prev_node = current_node
          current_node = next_node
      return prev_node
