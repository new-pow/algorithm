import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        // RT, CF, JM, AN
        Map<Character, Integer> scores = new HashMap<Character, Integer>(){{
            put('R', 0);
            put('T', 0);
            put('C', 0);
            put('F', 0);
            put('J', 0);
            put('M', 0);
            put('A', 0);
            put('N', 0);
        }};
        
        for (int i=0; i<survey.length; i++) {
            int temp = choices[i]-4;
            if (temp<0) {
                scores.replace(survey[i].charAt(0), scores.get(survey[i].charAt(0))+Math.abs(temp));
            }
            if (temp>0) {
                scores.replace(survey[i].charAt(1), scores.get(survey[i].charAt(1))+Math.abs(temp));
            }
        }
        
        // 출력
        String answer = (scores.get('R') >= scores.get('T')) ? "R" : "T";
        answer += (scores.get('C') >= scores.get('F')) ? "C" : "F";
        answer +=  (scores.get('J') >= scores.get('M')) ? "J" : "M";
        answer += (scores.get('A') >= scores.get('N')) ? "A" : "N";
        
        return answer;
    }
}