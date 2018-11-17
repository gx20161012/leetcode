class Solution{
	public String convert(String s, int nRows) {
        if(nRows == 1)return s;
        int len = s.length(), k = 0, interval = (nRows<<1)-2;
        char[] res = new char[len];
        for(int j = 0; j < len ; j += interval)//处理第一行
            res[k++] = s.charAt(j);
        for(int i = 1; i < nRows-1; i++)//处理中间行
        {
            int inter = (i<<1);
            for(int j = i; j < len; j += inter)
            {
                res[k++] = s.charAt(j);
                inter = interval - inter;
            }
        }
        for(int j = nRows-1; j < len ; j += interval)//处理最后一行
            res[k++] = s.charAt(j);
        return  new String(res);
    }
	public static void main(String[] args) {
		System.out.println(new Solution().convert("PAYPALISHIRING", 3));
	}
}
