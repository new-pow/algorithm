class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length];
        int j=0;
        for (int i=0; i<num_list.length; i++) {
            j = Math.abs(num_list.length-i)-1;
            answer[i] = num_list[j];
        }
        return answer;
    }
}