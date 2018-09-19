import java.util.ArrayList;
import java.util.List;
/**
 * Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
 * @author gaoxiang
 *
 */
class Solution {
    public List<List<Integer>> generate(int numRows) {
    	List<List<Integer>> list =new ArrayList<>();
    	for(int i = 1; i <= numRows; i++) {
    		List<Integer> l = new ArrayList<>();
    		if(i == 1) {
    			l.add(1);
    			list.add(l);
    			continue;
    		}
    		if(i == 2) {
    			l.add(1);
    			l.add(1);
    			list.add(l);
    			continue;
    		}
    		l.add(1);
    		for(int j=0; j<i-2; j++) {
    			l.add(list.get(i-2).get(j)+list.get(i-2).get(j+1));
    		}
    		l.add(1);
    		list.add(l);
    	}
        return list;
    }
    public static void main(String[] args) {
    	List<List<Integer>> list = new Solution().generate(5);
    	for(int i=0;i<5;i++) {
    		List<Integer> l =list.get(i);
    		for(int j = 0; j<l.size(); j++) {
    			System.out.print(l.get(j)+" ");
    		}
    		System.out.println();
    	}
	}
}