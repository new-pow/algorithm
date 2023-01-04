import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for (int i=0; i<t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            
            int num =1;
            for (int j=0; j<b; j++) {
                num = num * a %10;
            }
            
            if (num!=0) {
                System.out.println(num);
            } else {
                System.out.println(10);
            }
        }
    }
}