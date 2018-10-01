public class Solution {
    public ListNode reverseList(ListNode head) {
    	if (head == null) {
			return null;
		}
    	ListNode p = head.next;
    	ListNode q = head;
    	q.next = null;
    	ListNode temp = null;
    	while(p != null) {
    		temp = p.next;
    		p.next = q;
    		q = p;
    		p = temp;
    	}
    	return q;
    }
    public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head .next = new ListNode(2);
		head.next.next = new ListNode(3);
		ListNode root = new Solution().reverseList(head);
		while(root != null) {
			System.out.println(root.val);
			root = root.next;
		}
	}
}
class ListNode {
	int val;
	ListNode next;
	ListNode(int x) { 
		val = x; 
	}
}
