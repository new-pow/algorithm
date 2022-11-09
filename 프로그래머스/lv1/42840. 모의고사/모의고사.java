import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[] person1 = {1,2,3,4,5};
        int[] person2 = {2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] scores = new int[3];
        
        for (int i=0; i<answers.length; i++) {
            if (answers[i]==person1[i%person1.length]) scores[0] ++;
            if (answers[i]==person2[i%person2.length]) scores[1] ++;
            if (answers[i]==person3[i%person3.length]) scores[2] ++;
        }
        int max = Math.max(scores[0],scores[1]);
        max = Math.max(scores[2],max);
        
        int count = 0;
        for (int score : scores) {
            if(max==score) {
                count ++;
            }
        }
        
        int[] answer = new int[count];
        int idx = 0;
        for (int i=0; i<scores.length; i++) {
            if(max==scores[i]) {
                answer[idx++] = i+1;
            }
        }
        
        return answer;
    }
}