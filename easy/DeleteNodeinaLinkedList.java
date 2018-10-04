public class Solution {
	public void deleteNode(ListNode node) {
		node.val = node.next.val;
		node.next = node.next.next;
	}
    public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(3);
		head.next.next.next = new ListNode(4);
		Solution s = new Solution();
		s.deleteNode(head.next);
	}
}
class ListNode {
	int val;
	ListNode next;
	ListNode(int x) { 
		val = x; 
	}
}