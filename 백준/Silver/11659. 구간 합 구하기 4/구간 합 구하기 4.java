import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        // n,m 입력
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        
        int n = Integer.parseInt(stringTokenizer.nextToken());
        int m = Integer.parseInt(stringTokenizer.nextToken());
        
        // 수 배열 만들기
        stringTokenizer = new StringTokenizer(bufferedReader.readLine());
        int[] sums = new int[n+1];
        for (int i=1; i<n+1; i++){
           sums[i] = sums[i-1] + Integer.parseInt(stringTokenizer.nextToken());
        }
        // i,j 입력 및 출력
        for (int a=0; a<m; a++){
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            int i = Integer.parseInt(stringTokenizer.nextToken());
            int j = Integer.parseInt(stringTokenizer.nextToken());
            System.out.println(sums[j]-sums[i-1]);
        }
    }
}