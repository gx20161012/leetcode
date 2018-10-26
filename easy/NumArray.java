class NumArray {
	
	public int[] nums;
    public NumArray(int[] nums) {
        this.nums = nums;
    }
    
    public int sumRange(int i, int j) {
    	int sum = 0;
        if(i >= 0 && j < nums.length) {
        	for(int k = i ; k <  j + 1; k++) {
        		sum += nums[k];
        	}
        }else if(i < 0 && j < nums.length) {
        	for(int k = 0; k < j + 1; k++) {
        		sum += nums[k];
        	}
        }else if(i < 0 && j >= nums.length) {
        	for(int k = 0; k < nums.length; k++) {
        		sum += nums[k];
        	}
        }else if(i >= 0 && j >= nums.length) {
        	for(int k = i; k < nums.length; k++) {
        		sum += nums[k];
        	}
        }
        return sum;
    }
}
