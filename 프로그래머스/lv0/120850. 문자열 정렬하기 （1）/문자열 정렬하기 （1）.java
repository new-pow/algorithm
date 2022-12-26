import java.util.*;

class Solution {
    public List<Integer> solution(String my_string) {
        List<Integer> answer = new ArrayList<>();
        for (int i=0; i<my_string.length(); i++) {
            char letter = my_string.charAt(i);
            if (Character.isDigit(letter)) answer.add(letter-48);
        }
        if (answer.size() >0) Collections.sort(answer);
        
        return answer;
    }
}