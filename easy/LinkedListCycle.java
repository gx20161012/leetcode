/**
 * Given a linked list, determine if it has a cycle in it.
 * @author gaoxiang
 *
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
    	if(head == null) {
    		return false;
    	}
    	ListNode slow = head;
    	ListNode fast = head;
    	while(slow != null) {
    		if(slow.next == null) {
    			return false;
    		}else {	
    			slow = slow.next;
    		}
    		if(fast.next == null||fast.next.next == null) {
    			return false;
    		}else {
    			fast = fast.next.next;	
    		}
    		if(fast == slow) {
    			return true;
    		}
    	}
        return false;
    }
    public static void main(String[] args) {
		ListNode head = new ListNode(0);
		ListNode first = new ListNode(1);
		ListNode second = new ListNode(2);
		ListNode third = new ListNode(3);
		ListNode fourth = new ListNode(4);
		ListNode fifth = new ListNode(5);
		head.next = null;
		first.next = null;
		second.next = third;
		third.next = fourth;
		fourth.next = fifth;
		fifth.next = null;
		
		System.out.println(new Solution().hasCycle(head));
	}
}
class ListNode {
     int val;
     ListNode next;
     ListNode(int x) {
         val = x;
         next = null;
     }
}
