/**
 * Write a program to find the node at which the intersection of 
 * two singly linked lists begins.
 * @author gaoxiang
 *
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
    	if(headA==null||headB==null) {
    		return null;
    	}
    	ListNode p = headA;
    	ListNode q = headB;
    	int a = getLength(headA);
    	int b = getLength(headB);
    	if(a > b) {
    		for(int i = 0; i < a - b; i++) {
    			p = p.next;
    		}
    	}else {
    		for(int i = 0;i < b - a; i++) {
    			q = q.next;    			
    		}
		}
    	while(p!=null&&q!=null) {
    		if(p == q) {
    			return p;
    		}
    		p=p.next;
    		q=q.next;
    	}
        return null;
    }
    public int getLength(ListNode head) {
    	int length = 0;
    	if(head == null) {
    		return 0;
    	}
    	while(head != null) {
    		length += 1;
    		head = head.next;
    	}
    	return length;
    }
    public static void main(String[] args) {
		
	}
}
class ListNode {
	int val;
	ListNode next;
	ListNode(int x) {
		next = null;     
	}
}

