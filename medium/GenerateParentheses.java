import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> generateParenthesis(int n) {
    	List<String> list = new ArrayList<>();
    	generate(n, n, "", list);
    	return list;
    }
    public void generate(int left, int right, String string, List<String> list) {
		if(left < 0 || right < 0 || left > right)
			return;
		if(left == 0 && right == 0) {
			list.add(string);
			return;
		}
		generate(left-1, right, string+"(", list);
		generate(left, right-1, string+")", list);
	}
    public static void main(String[] args) {
		System.out.println(new Solution().generateParenthesis(2));
	}
}
