import java.util.*;

class Solution {
    public long solution(long n) {
        double sqrt = Math.sqrt(n);
        
        if (sqrt == (int) sqrt) return (long)((sqrt+1)*(sqrt+1));
        return -1;
    }
}