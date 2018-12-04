class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
    	int length = 0;
    	ListNode p = head; 
    	while(p != null) {
    		length ++;
    		p = p.next;
    	}
    	int index = length - n;
    	if(index == 0) {
    		head = head.next;
    		return head;
    	}
    	int count = 0;
    	p = head;
    	while(p != null) {
    		count ++;
    		if(index == count) {
    			p.next = p.next.next;
    			break;
    		}
    		p = p.next;
    	}
        return head;
    }
    public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next = new ListNode(3);
		head.next.next.next = new ListNode(4);
		head.next.next.next.next = new ListNode(5);
		
		ListNode root = new Solution().removeNthFromEnd(head, 5);
		while(root != null) {
			System.out.print(root.val+" ");
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
