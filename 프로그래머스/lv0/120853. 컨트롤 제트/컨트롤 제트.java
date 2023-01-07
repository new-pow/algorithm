import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (String letter : s.split(" ")) {
            if (letter.equals("Z")) {
                stack.pop();
            } else {
                stack.push(Integer.parseInt(letter));
            }
        }
        
        while (!stack.isEmpty()) {
            answer += stack.pop();
        }
        return answer;
    }
}