class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] sChars = new int[256];
        int[] tChars = new int[256];

        for(int i = 0;i < s.length();++i){
            if(sChars[s.charAt(i)] != tChars[t.charAt(i)]){
                return false;
            }else{
                sChars[s.charAt(i)] = tChars[t.charAt(i)] = t.charAt(i);
            }
        }

        return true;
    }
    public static void main(String[] args) {
		String s = "egg";
		String t = "add";
		System.out.println(new Solution().isIsomorphic(s, t));
	}
}

