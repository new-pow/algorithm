class Solution {
    public String solution(int age) {
        char[] charList = new char[10];
        for (int i=0; i<charList.length; i++) {
            charList[i] = (char)('a'+ i);
        }
        
        StringBuilder answer = new StringBuilder();
        while(age>0) {
            answer.append(String.valueOf(charList[age%10]));
            age /= 10;
        }
        return answer.reverse().toString();
    }
}