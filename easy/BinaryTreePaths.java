import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> list = new ArrayList<>();
        if(root == null) {
        	return list;
        }
        List<String> left = binaryTreePaths(root.left);
        List<String> right = binaryTreePaths(root.right);
        
        for(String path:left) {
        	list.add(root.val+"->"+path);
        }
        for(String path:right) {
        	list.add(root.val+"->"+path);
        }
        if(list.size()==0) {
        	list.add(""+root.val);
        }
        return list;
    }
    public String list2string(List<Integer> list) {
    	String string = String.valueOf(list.get(0));
    	for(int i = 1; i < list.size(); i++) {
    		string = string + "->" + list.get(i);
    	}
    	return string;
    }
}
class TreeNode {
	int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { 
    	val = x; 
    }
}
