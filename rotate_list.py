#given the head of a linked list, rotate the list to the right by k places.
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        
        # Make the linked list circular
        current.next = head
        
        # Find the new tail: (length - k % length - 1)th node
        # and the new head: (length - k % length)th node
        k = k % length
        new_tail_position = length - k - 1
        new_tail = head
        
        for _ in range(new_tail_position):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        
        # Break the circle
        new_tail.next = None
        
        return new_head