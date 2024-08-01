# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = ListNode(float('-inf'))
        for li in lists:
            if li:
                result= self.merge(result, li)
        return result.next
    def merge(self, ptr1, ptr2):
        dummy= ListNode(float('-inf')) #cuz we need sm to pt at beginning
        curr= dummy #to traverse
        while ptr1 and ptr2: #if both exists, just point the ponter no other thing 
            if ptr1.val<=ptr2.val:
                curr.next= ptr1
                ptr1=ptr1.next
            else:
                curr.next=ptr2
                ptr2=ptr2.next
            curr=curr.next
        if ptr1:
            curr.next= ptr1
        else:
            curr.next=ptr2
        
        return dummy.next #cuz we created a fake node in the begg, pt to next for original vals

        #complxity-  k lists, with n length each means for each k we're traversing it once normally, next after merging with the thing, until it runs out
        #n+2n+3n...nk^2 
        #space- o(1) 

        