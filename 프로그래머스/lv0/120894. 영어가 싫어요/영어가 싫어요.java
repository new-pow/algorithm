import java.util.*;

class Solution {
    
    String[] num = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    
    public long solution(String numbers) {
        long answer = 0;
        
        for (int i=0; i<num.length; i++) {
            numbers = numbers.replaceAll(num[i], String.valueOf(i));
        }
        
        return Long.parseLong(numbers);
    }
}