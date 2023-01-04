import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        String[] colors = {"black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"};
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        String first = br.readLine();
        String second = br.readLine();
        String third = br.readLine();
        
        int num = 0;
        int multiply = 0;
        
        for (int i=0; i<colors.length; i++) {
            if (first.equals(colors[i])) num += i*10;
            if (second.equals(colors[i])) num += i;
            if (third.equals(colors[i])) multiply = i;
        }
        
        if (num != 0) {
            // 문자열이 계속 변할거라 StringBuilder 클래스 사용
            StringBuilder answer = new StringBuilder(String.valueOf(num));
        
            for (int i=0; i<multiply; i++) {
                answer.append("0");
            }
        
            System.out.println(answer.toString());
        } else {
            System.out.println(0);
        }
    }
}