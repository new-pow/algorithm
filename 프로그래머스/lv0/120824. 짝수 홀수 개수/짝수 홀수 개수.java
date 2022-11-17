class Solution {
    public int[] solution(int[] num_list) {
        int odd=0;
        int even=0;
        for (int num : num_list) {
            if (num%2==0) even++;
            if (num%2==1) odd++;
        }
        int[] arr = {even, odd};
        return arr;
    }
}