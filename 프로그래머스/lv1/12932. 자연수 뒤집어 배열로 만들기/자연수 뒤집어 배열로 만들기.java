import java.util.*;

class Solution {
    public int[] solution(long n) {
        List<Integer> answer = new ArrayList<>();
        while (n>0) {
            answer.add((int)(n%10));
            n /= 10;
        }
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}