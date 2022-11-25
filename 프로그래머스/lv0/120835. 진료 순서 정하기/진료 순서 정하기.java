import java.util.*;

class Solution {
    public int[] solution(int[] emergency) {
        int[] copy = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(emergency);
        int[] answer = new int[emergency.length];
        int rank = 1;
        
        for (int j=0; j<emergency.length; j++) {
            for (int i=0; i<emergency.length; i++) {
                if (copy[j]==emergency[i]) {
                    answer[j] = emergency.length-i;
                }
            }
        }
        
        return answer;
    }
}