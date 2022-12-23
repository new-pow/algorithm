import java.util.*;

class Solution {
    public String solution(String my_string) {
        List<String> moum = Arrays.asList("a", "e", "i", "o", "u");
        for (int i=0; i<moum.size(); i++) {
            my_string = my_string.replace(moum.get(i), "");
        }
        return my_string;
    }
}