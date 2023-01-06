class Solution {
    public int solution(int num, int k) {
        String numStr = Integer.toString(num);
        String kStr = Integer.toString(k);
        if (numStr.indexOf(kStr)==-1) {
            return -1;
        } else {
            return numStr.indexOf(kStr)+1;
        }
    }
}