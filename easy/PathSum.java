class Solution {
	public boolean hasPathSum(TreeNode root, int sum) {
		if(root == null) {
			return false;
		}
		if(root.left == null && root.right == null && sum-root.val == 0) {
			return true;
		}
		return hasPathSum(root.left, sum-root.val) || hasPathSum(root.right, sum-root.val);
	}
    public static void main(String[] args) {
		TreeNode root = null;
//		root.left = new TreeNode(9);
//		root.right = new TreeNode(20);
//		root.right.left = new TreeNode(15);
//		root.right.right = new TreeNode(7);
		System.out.println(new Solution().hasPathSum(root, 1));
	}
}
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x){ 
    	val = x; 
    }
}
