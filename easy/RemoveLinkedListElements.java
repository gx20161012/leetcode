class Solution {
    public ListNode removeElements(ListNode head, int val) {
    	if (head == null)
    		return head;
        ListNode p = head;
        ListNode q = head;
        while(p != null) {
        	if(p.val == val && head == p) {
        		head = p.next;
        		q = head;
        		p = p.next;
        	}else if(p.val == val){
        		q.next = p.next;
        		p = p.next;
        	}else {
        		q = p;
        		p = p.next;
        	}
        }
        return head;
    }
    public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(1);
		head.next.next = new ListNode(2);
		head.next.next.next = new ListNode(3);
    	ListNode root = new Solution().removeElements(head, 1);
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

