class Solution {
    public int getSum(int a, int b) {
    	while(b != 0) {
    		int c = a ^ b;
    		b = (a & b) << 1;
    		a = c;
    	}
    	return a;
    }
    public static void main(String[] args) {
		int a = 20;
		int b = 2;
		int c = a ^ b;
		int d = a & b;
		System.out.println(c);
		System.out.println(d);
		System.out.println(new Solution().getSum(a, b));
	}
}
