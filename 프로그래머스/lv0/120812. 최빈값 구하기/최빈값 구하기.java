class Solution {
    public int solution(int[] array) {
        int[] arr = new int[1000];
        int max = 0;
        int answer = 0;
        
        for (int i : array) {
            arr[i] ++;
            if (max==arr[i]) {
                answer = -1;
            } else if (max<arr[i]) {
                max = arr[i];
                answer = i;
            }
        }
        
        return answer;
    }
}