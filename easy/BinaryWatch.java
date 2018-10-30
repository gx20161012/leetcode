import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> readBinaryWatch(int num) {
    	List<String> list = new ArrayList<>();
    	if(num < 0) {
    		return list;
    	}
    	for(int i = 0; i < 12; i++) {
    		for(int j = 0; j < 60; j++) {
    			if(Integer.bitCount(i) + Integer.bitCount(j) == num) {
    				list.add(String.format("%d:%02d", i, j));
    			}
    		}
    	}
        return list;
    }
    public static void main(String[] args) {
		System.out.println(new Solution().readBinaryWatch(1));
	}
    
}
