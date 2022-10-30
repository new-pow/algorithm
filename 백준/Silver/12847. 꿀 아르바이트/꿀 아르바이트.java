import java.util.*;
import java.io.*;

public class Main{
     public static void main(String[] args) throws IOException{
         // 입력
         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
         StringTokenizer st = new StringTokenizer(br.readLine());
         int n = Integer.parseInt(st.nextToken());
         int m = Integer.parseInt(st.nextToken());
         
         st = new StringTokenizer(br.readLine());
         int[] payment = new int[n];
         for (int i=0; i<n; i++) payment[i] = Integer.parseInt(st.nextToken());

         // 변수 설정
         long sum = 0; // m일 급여 합계

         // 초기화
         for (int i=0; i<m; i++) {
             sum += payment[i];
         }
         
         long sumMax = sum; // m일 급여 합계 최대값

         for(int j=m; j<n; j++){
             // 시작 - , 종료급여 +
             sum += (payment[j]-payment[j-m]);

             // 비교
             sumMax = Math.max(sumMax, sum);
         }
         System.out.println(sumMax);
     }
}