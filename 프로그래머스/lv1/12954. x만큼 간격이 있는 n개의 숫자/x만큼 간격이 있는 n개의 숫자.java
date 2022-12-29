class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for (long l=0; l<n; l++) {
            answer[(int)l] = x + (x*l);
        }
        return answer;
    }
}