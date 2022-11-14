class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i=1; i<=n*6; i++) {
            if(i%6==0 && i%n==0) {answer = i/6; break;}
        }
        return answer;
    }
}