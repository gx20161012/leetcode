
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	if(l1 == null) {
    		return l2;
    	}else if(l2 == null) {
    		return l1;
    	}
    	ListNode p = l1.next;
    	ListNode q = l2.next;
    	int add = (l1.val+l2.val)%10;
    	int carry = 0;
    	if((l1.val + l2.val) > 9) {
    		carry = 1;
    	}
    	ListNode head = new ListNode(add);
    	ListNode r = head;
    	while(p != null || q != null) {
    		if(p != null && q != null) {
    			ListNode temp = new ListNode((p.val + q.val + carry)%10);
    			r.next = temp;
    			r = temp;
    			if((p.val + q.val + carry) > 9) {
    				carry = 1;
    			}else {
    				carry = 0;
    			}
    			p = p.next;
    			q = q.next;
    		}else if(p == null || q != null) {
    			ListNode temp = new ListNode((q.val + carry)%10);
    			r.next = temp;
    			r = temp;
    			if((q.val + carry) > 9) {
    				carry = 1;
    			}else {
    				carry = 0;
    			}
    			q = q.next;
    		}else if(p != null || q == null) {
    			ListNode temp = new ListNode((p.val + carry)%10);
    			r.next = temp;
    			r = temp;
    			if((p.val + carry) > 9) {
    				carry = 1;
    			}else {
    				carry = 0;
    			}
    			p = p.next;
    		}
    	}
    	if(carry == 1) {
    		ListNode s = head;
    		while(s.next != null) {
    			s = s.next;
    		}
    		s.next = new ListNode(1);
    	}
        return head;
    }
    public static void main(String[] args) {
		ListNode l1 = new ListNode(9);
		ListNode l2 = new ListNode(9);
		l1.next = new ListNode(9);
		l2.next = new ListNode(9);
		ListNode head = new Solution().addTwoNumbers(l1, l2);
		while(head != null) {
			System.out.print(head.val + "--->");
			head = head.next;
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
