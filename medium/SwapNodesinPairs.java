class Solution {
    public ListNode swapPairs(ListNode head) {
    	if(head==null || head.next==null)   
    		return head;
    	
        ListNode dummy = new ListNode(-1);
        
        ListNode temp = dummy, temp1=head;
        
        while(temp1!=null && temp1.next!=null){
            temp.next = temp1.next;
            ListNode temp2 = temp1.next.next;
            temp.next.next = temp1;
            temp1.next = temp2;
            temp=temp1;
            temp1=temp.next;
        }
        
        return dummy.next;
    }
    public static void main(String[] args) {
		ListNode head = new ListNode(1);
		head.next = new ListNode(2);
		head.next.next  = new ListNode(3);
		head.next.next.next = new ListNode(4);
		head.next.next.next.next = new ListNode(5);
		head.next.next.next.next.next = new ListNode(6);
		
		ListNode root = new Solution().swapPairs(head);
		
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
