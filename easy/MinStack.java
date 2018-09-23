import java.util.ArrayList;
import java.util.List;

class MinStack {

	public List<Integer> list = null; 
    /** initialize your data structure here. */
    public MinStack() {
        this.list = new ArrayList<>();
    }
    
    public void push(int x) {
        list.add(x);
    }
    
    public void pop() {
    	if(list.size()!=0) {
    		list.remove(list.size()-1);
    	}
    }
    
    public int top() {
    	if(list.size()!=0) {
    		return list.get(list.size()-1);
    	}else {
    		return -100000000;
    	}
    }
    
    public int getMin() {
    	int min = Integer.MAX_VALUE;
    	if(list.size()!=0) {
    		for(int i = 0; i<list.size(); i++) {
    			if(min>list.get(i)) {
    				min = list.get(i);
    			}
    		}
    	}
    	return min;
    }
    
    public static void main(String[] args) {
    	MinStack minStack = new MinStack();
    	minStack.push(-2);
    	minStack.push(0);
    	minStack.push(-3);
    	System.out.println(minStack.getMin());   //--> Returns -3.
    	minStack.pop();
    	System.out.println(minStack.top());      //--> Returns 0.
    	System.out.println(minStack.getMin());   //--> Returns -2.
	}
}
