import java.util.HashSet;
import java.util.Set;

class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    	if (head == null)
    		return null;
    	Set<Integer> set = new HashSet<>();
    	ListNode pListNode = head.next;
    	ListNode pre = head;
    	set.add(head.val);
    	while(pListNode != null) {
    		if(!set.contains(pListNode.val)) {
    			set.add(pListNode.val);
    			pre = pListNode;
    			pListNode = pListNode.next;
    		}else {
    			ListNode qListNode = pListNode.next;
    			pre.next = qListNode;
    			pListNode = pListNode.next;
    		}
    	}
        return head;
    }
}
