import java.util.*;
import java.io.*;

public class Main{
    
    static int c;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        
        long result = pow(a,b);
        
        System.out.println(result);
    }
    
    public static long pow(long a, long b) {
        if (b==1) {return (long)a%c;}
        long temp = pow(a,b/2);
        
        if (b%2 == 1) {
            return (temp*temp)%c*(a%c)%c;
        }
        return (temp*temp)%c;
    }
}