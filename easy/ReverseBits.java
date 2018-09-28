public class Solution {
   public int reverseBits(int input) {
       int result = 0;
       for (int i = 0; i < 32; i++) {      // 一共32位
           if (((input >> i) & 1) == 1) {  // 如果移位后最右位为1
               int j = 31 - i;             // 判断当前是第几位，并换算成反转后的位数
               result |= 1 << j;           // 得知是反转后第几位，存入结果result中
           }
       }
       return result;
   }
}
