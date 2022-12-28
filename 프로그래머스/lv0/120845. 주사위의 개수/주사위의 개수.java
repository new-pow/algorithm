import java.util.*;

class Solution {
    public int solution(int[] box, int n) {
        // 가로, 세로, 높이
        // 주사위 모서리 길이 n
        int garo = box[0]/n;
        int sero = box[1]/n;
        int high = box[2]/n;
        return garo*sero*high;
    }
}