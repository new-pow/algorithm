import java.util.*;

class Solution {
    public int solution(String A, String B) {
        int answer = 0;
        
        while (!A.equals(B)) {
            answer ++;
            
            if (answer > A.length() ) {
                return -1;
            }
            
            String letters =  A.substring(0,A.length()-1);
            String lastLetter =  A.substring(A.length()-1);
            
            A = lastLetter + letters;
        }
            
        return answer;
    }
}