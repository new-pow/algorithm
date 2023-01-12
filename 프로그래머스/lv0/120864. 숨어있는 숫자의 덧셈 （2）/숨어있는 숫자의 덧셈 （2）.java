import java.util.*;

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        
        String[] numbers = my_string.replaceAll("[^0-9]", " ").split(" ");
        
        for (String s : numbers) {
            if (s.equals("")) {
                continue;
            } else {
                answer += Integer.parseInt(s.trim());
            }
        }
        
        return answer;
    }
}