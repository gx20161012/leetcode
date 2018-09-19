/**
 * Given an array where elements are sorted in ascending order, 
 * convert it to a height balanced BST.
 * @author gaoxiang
 *
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
    	if(nums.length == 0) {
    		return null;
    	}
    	if(nums.length == 1) {
    		return new TreeNode(nums[0]);
    	}
    	int length = nums.length;
        TreeNode root = new TreeNode(nums[length/2]);
        int[] nums1 = null;
    	int[] nums2 = null;
		 if(length % 2 ==0) {
	        	nums1 = new int[length/2];
	        	nums2 = new int[length/2-1];
	        	for(int i=0; i<length/2; i++) {
	        		nums1[i] = nums[i];
	        	}
	        	int j=0;
	        	for(int i = length/2+1; i<length; i++) {
	        		nums2[j] = nums[i];
	        		j++;
	        	}
	        }else {
	        	nums1 = new int[length/2];
	        	nums2 = new int[length/2];
	        	for(int i=0; i<length/2; i++) {
	        		nums1[i] = nums[i];
	        	}
	        	int j=0;
	        	for(int i = length/2+1; i<length; i++) {
	        		nums2[j] = nums[i];
	        		j++;
	        	}
			}
        
        root.left = sortedArrayToBST(nums1);
        root.right = sortedArrayToBST(nums2);
        
        return root;
    }
    public static void main(String[] args) {
		int[] nums = {-12,-10,-3,0,5,9};

		TreeNode root = new Solution().sortedArrayToBST(nums);
		System.out.println(root.val);
		System.out.println(root.left.val);
		System.out.println(root.right.val);
		System.out.println(root.left.left.val);
		System.out.println(root.left.right.val);
		System.out.println(root.right.left.val);
	}
}
class TreeNode {
	int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { 
    	val = x; 
 }
