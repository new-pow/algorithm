import java.util.*;

class Solution {
    public int solution(String[] s1, String[] s2) {
        int answer = 0;
        for (int i=0; i<s2.length; i++) {
            String matchStr = s2[i];
            if (Arrays.stream(s1).anyMatch(s -> s.equals(matchStr))) answer ++;
        }
        return answer;
    }
}