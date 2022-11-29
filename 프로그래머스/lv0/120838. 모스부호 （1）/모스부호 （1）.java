class Solution {
    public String solution(String letter) {
        String answer = "";
        String[] mos = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        String[] letters = letter.split(" ");
        
        for (int i=0; i<letters.length; i++) {
            for (int j=0; j<mos.length; j++) {
                char c = (char)('a'+j);
                if (letters[i].equals(mos[j])) letters[i] = String.valueOf(c);
            }
        }
        answer = String.join("", letters);
        return answer;
    }
}