import java.util.*;
import java.io.*;

public class Main{
   public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i=0; i<n; i++){
            int temp = 0;
            int answer =0 ;
            String s = br.readLine();
            char[] arrC = s.toCharArray();

            for (char c : arrC) {
                if (c == 'O'){
                    temp++;
                } else {
                    temp = 0;
                }
                answer += temp;
            }
            System.out.println(answer);
        }

    }
}