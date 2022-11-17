import java.io.*;
import java.util.*;

public class Main{
    
    static int[] arr;
    
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n+1];
        System.out.println(dp(n));
    }
    
    private static int dp(int n) {
        if (n==1) { return 1; }
        else if (n==2) { return 2; }
        else if (arr[n]==0) {
            arr[n] = (dp(n-1)+dp(n-2))%15746;
        }
        return arr[n];
    }
}