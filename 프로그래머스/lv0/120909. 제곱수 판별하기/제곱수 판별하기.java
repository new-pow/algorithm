import java.util.*;

class Solution {
    public int solution(int n) {
        int answer1 = (int)(Math.sqrt(n)*10);
        int answer2 = (int)(Math.sqrt(n))*10;
        if (answer1 == answer2) return 1;
        return 2;
    }
}