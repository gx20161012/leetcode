package com.nju.test;

/**
 * Given a binary tree, 
 * check whether it is a mirror of itself (ie, symmetric around its center).
 * @author gaoxiang
 *
 */
class Solution {
    public boolean isSymmetric(TreeNode root) {
    	if(root != null) {
    		return isSymmetricHelp(root.left,root.right);
    	}else {
    		return true;
    	}
    }
    private boolean isSymmetricHelp(TreeNode left, TreeNode right) {
    	if(left == null && right ==null) {
    		return true;
    	}
    	if(left == null || right == null) {
    		return false;
    	}
    	if(left.val != right.val) {
    		return false;
    	}
		return isSymmetricHelp(left.right, right.left) && isSymmetricHelp(left.left, right.right);
	}
	public static void main(String[] args) {
    	TreeNode root = new TreeNode(1);
    	System.out.println(new Solution().isSymmetric(root));
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
