class Solution {
    public int minDepth(TreeNode root) {
        if(root == null) {
        	return 0;
        }
        else if(root.left == null && root.right == null) {
        	return 1;
        }
        else if(root.left != null && root.right == null) {
        	return 1+minDepth(root.left);
        }
        else if(root.left == null && root.right != null) {
        	return 1+minDepth(root.right);
        }
        return Math.min(1+minDepth(root.left), 1+minDepth(root.right));
    }
    public static void main(String[] args) {
		TreeNode root = new TreeNode(3);
		//root.left = new TreeNode(9);
		root.right = new TreeNode(20);
		root.right.left = new TreeNode(15);
		root.right.right = new TreeNode(7);
		System.out.println(new Solution().minDepth(root));
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
