class Solution {
    public TreeNode invertTree(TreeNode root) {
    	if(root == null) {
    		return null;
    	}
    	TreeNode temp = root.left;
    	root.left = invertTree(root.right);
    	root.right = invertTree(temp);
        return null;
    }
    public static void main(String[] args) {
		
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