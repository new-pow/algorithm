import java.util.*;

class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String format = "^[0-9]$";
        
        for (int i=0; i<my_string.length(); i++) {
            String letter = String.valueOf(my_string.charAt(i));
            if ( letter.matches(format) ) answer += Integer.parseInt(letter);
        }
        
        return answer;
    }
}