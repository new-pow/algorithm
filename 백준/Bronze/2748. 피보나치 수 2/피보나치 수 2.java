import java.util.*;
import java.io.*;

public class Main{
    static Long[] arr;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new Long[n+1];
        
        arr[0] = 0L;
        arr[1] = 1L;
        System.out.println(dp(n));
    }
    
    public static long dp (int x) {
        if (arr[x] == null) {
            arr[x] = dp(x-1)+dp(x-2);
        }
        return arr[x];
    }
}