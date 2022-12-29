class Solution {
    public boolean solution(int x) {
        int origin = x;
        int jari = 0;
        while(x>0) {
            jari += x%10;
            x /= 10;
        }
        return origin%jari==0;
    }
}