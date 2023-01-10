import java.util.*;

class Solution {
    public String solution(String my_string) {
        char[] cArr = my_string.toCharArray();
        for (int i=0; i<cArr.length; i++) {
            if(cArr[i] < 'a') {
                cArr[i] += 32;
            }
        }
        Arrays.sort(cArr);
        
        return String.valueOf(cArr);
    }
}