class Solution {
    public int[] solution(int denum1, int num1, int denum2, int num2) {
        // 기약분수
        // a1/a2 + b1/b2 = ((a1*b2)+(b1*a2))/a2*b2
        int top = (denum1 * num2) + (denum2 * num1);
        int bottom = (num1 * num2);
        int temp = 1;
        
        for (int i=2; i<=Math.max(top, bottom); i++) {
            if (top%i==0 && bottom%i==0) { // 최대 공약수
                temp = i;
            }
        }
        int[] answer = {top/temp, bottom/temp};
        
        return answer;
    }
}