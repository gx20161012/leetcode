class Solution {
    public int divide(int dividend, int divisor) {
    	if (divisor == 0 || (dividend == -2147483648 && divisor == -1)) 
    		return 2147483647;
        int result = 0;
        boolean flag = (dividend < 0 && divisor > 0) || (dividend > 0 && divisor < 0);
        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        if(a < b) {
             return 0;
        }
        long sum = 0;
        long pow = 0;
        while(a >= b) {
            sum = b;
            pow = 1;
            while(2*sum <= a) {
            	sum += sum;
            	pow += pow;
            }
            a -= sum;
            result += pow;
           }
        return flag ? - result : result;
        
    }
}
