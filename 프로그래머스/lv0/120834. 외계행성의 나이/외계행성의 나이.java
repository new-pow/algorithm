class Solution {
    public String solution(int age) {
        String answer = "";
        
        String str = age+"";
        for(int i=0; i<str.length(); i++){
            answer+=(char)(str.charAt(i)+49);
        }

        return answer;
    }
}