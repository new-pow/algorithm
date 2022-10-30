import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        boolean[] arr = new boolean[2001];
        for (int i=0; i<n; i++){
            arr[Integer.parseInt(br.readLine())+1000] = true;
        }
        // 정렬안해도됨
        for(int i = 0; i < 2001; i++) {
            if(arr[i]){
                sb.append(i-1000).append('\n');
            }
        }
        System.out.println(sb);
    }
}