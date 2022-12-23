import java.util.*;

class Solution {
    public List<Integer> solution(int n, int[] numlist) {
        List<Integer> answer = new ArrayList<>();
        
        for (int i : numlist) {
            if (i%n == 0) answer.add(i);
        }
        
        return answer;
    }
}