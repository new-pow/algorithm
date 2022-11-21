import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        
        int[] coins = new int[n];
        
        for (int i=0; i<n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }
        
        int result = 0;
        
        for (int i=n-1; i>=0; i--) {
            if (k<coins[i]) continue;
            else if (k>=coins[i]) {
                result += k/coins[i];
                k = k%coins[i];
            }
        }
        System.out.println(result);
    }
}