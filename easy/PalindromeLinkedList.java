public class Solution {
	public boolean isPalindrome(ListNode head) {
		if(head == null || head.next == null)
			return true;
		ListNode slow = head, fast = head;
		while(fast.next != null && fast.next.next != null) {
			slow = slow.next;
			fast = fast.next.next;
		}
		ListNode middle = slow.next;
		ListNode pre = head;
		while(middle.next != null) {
			ListNode temp = middle.next;
			middle.next = temp.next;
			temp.next = slow.next;
			slow.next = temp;
		}
		while(slow.next != null) {
			slow = slow.next;
			if(pre.val != slow.val)
				return false;
			pre = pre.next;
		}
		return true;
	}
}