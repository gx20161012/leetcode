/**
 * Merge two sorted linked lists and return it as a new list. 
 * The new list should be made by splicing together the nodes of the first two lists.
 * Input: 1->2->4, 1->3->4
 * Output: 1->1->2->3->4->4
 * @author gao xiang
 *
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
    	if(l1 == null) return l2;
		if(l2 == null) return l1;
		ListNode l3 = null;
		if(l1.val < l2.val) {
			l3= l1;
			l1 = l1.next;
		}else {
			l3 = l2;
			l2 = l2.next;
		}
		ListNode p = l3;
		while(l1!=null || l2!=null) {
			if(l1!=null && l2!=null) {
				if(l1.val < l2.val) {
					p.next = l1; 
					l1 = l1.next;
					p = p.next;
				}else {
					p.next = l2;
					l2 = l2.next;
					p = p.next;
				}
			}else if(l1!=null && l2==null) {
				p.next = l1; 
				l1 = l1.next;
				p = p.next;
			}else if(l1==null && l2!=null) {
				p.next = l2;
				l2 = l2.next;
				p = p.next;
			}
		}
		return l3;
		
		
//		if(l1.val < l2.val){
//			l1.next = mergeTwoLists(l1.next, l2);
//			return l1;
//		}else{
//			l2.next = mergeTwoLists(l1, l2.next);
//			return l2;
//		}
    }
    public static void main(String[] args) {
		ListNode l1 = new ListNode(1);
		l1.next = new ListNode(2);
		l1.next.next = new ListNode(4);
		ListNode l2 = new ListNode(1);
		l2.next = new ListNode(3);
		l2.next.next = new ListNode(4);
		ListNode l3 = new Solution().mergeTwoLists(l1, l2);
		while(l3 != null) {
			System.out.println(l3.val);
			l3 = l3.next;
		}
	}
}
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

