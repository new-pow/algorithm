import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        String c = "";
        
        if (a-b > 0) c=">";
        if (a-b < 0) c="<";
        if (a-b == 0) c="==";
        
        System.out.println(c);
    }
}