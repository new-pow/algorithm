class Solution {
    public String solution(int a, int b) {
                int[] lastdays = {0,31,29,31,30,31,30,31,31,30,31,30,31};
        String[] days = {"THU","FRI","SAT","SUN","MON","TUE","WED"};

        int countDay = b;

        // 월 -> 일
        for (int i=0; i<a; i++) {
            int lastday = lastdays[i];
            countDay += lastday;
        }

        String day = days[countDay%7];
        return day;
    }
}