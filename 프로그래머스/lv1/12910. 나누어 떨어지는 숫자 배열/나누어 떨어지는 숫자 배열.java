import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        boolean[] checks = new boolean[arr.length];
        int count = 0;
        int[] answer;
        
        for (int i=0; i<arr.length; i++) {
            if (arr[i]%divisor==0) {
                checks[i] = true; count++;
            }
        }
        
        if (count==0) {
            answer = new int[1];
            answer[0] = -1;
        } else {
            answer = new int[count];
            int inputCount = 0;
            for (int i=0; i<arr.length; i++) {
                if (checks[i]) {
                    answer[inputCount] = arr[i];
                    inputCount ++;
                }
            }

            Arrays.sort(answer);
        }
        
        return answer;
    }
}