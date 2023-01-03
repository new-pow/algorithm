class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int[] answer = new int[2];
        int max_sero = board[1] / 2;
        int max_garo = board[0] / 2;
        
        for (String key : keyinput) {
            if (key.equals("up")) {
                answer[1] ++;
                if (answer[1] > max_sero) answer[1] = max_sero;
            } else if (key.equals("down")) {
                answer[1] --;
                if (answer[1] < max_sero*(-1)) answer[1] = max_sero*(-1);
            } else if (key.equals("left")) {
                answer[0] --;
                if (answer[0] < max_garo*(-1)) answer[0] = max_garo*(-1);
            } else {
                answer[0] ++;
                if (answer[0] > max_garo) answer[0] = max_garo;
                }
            }
        
        return answer;
    }
}