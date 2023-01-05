class Solution {
    public static int solution(String[] babbling) {
        String[] keyword = {"aya", "ye", "woo", "ma"};
        int answer = 0;

        for (String babble : babbling) {
            babble = replaceKeyword(keyword, babble);

            if (babble.matches("^[0-9]*$") && isContinuity(babble)) {
                answer++;
            }
        }

        return answer;
    }

    private static String replaceKeyword(String[] keyword, String babble) {
        for (int i = 0; i < keyword.length; i++) {
            babble = babble.replaceAll(keyword[i], String.valueOf(i));
        }
        return babble;
    }

    private static boolean isContinuity(String babble) {
        for (int i = 0; i < babble.length()-1; i++) {
            if (babble.charAt(i) == babble.charAt(i + 1)) {
                return false;
            }
        }
        return true;
    }
}