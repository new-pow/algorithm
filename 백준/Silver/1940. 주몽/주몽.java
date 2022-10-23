import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 재료 개수
        int m = Integer.parseInt(br.readLine()); // 고유 숫자
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        for (int i=0; i<n; i++) arr[i] = Integer.parseInt(st.nextToken());
    
        // 정렬하기
        Arrays.sort(arr);
        
        // 투포인터 위치 등 정의
        int s = 0;
        int e = n-1;
        int result = 0;
        
        // 포인터 이동원칙
        while(s < e) {
            if (arr[s] + arr[e] < m) { // 합 더 크게
                s ++;
            } else if(arr[s] + arr[e] >m) { // 합 더 작게
                e --;
            } else { // sum==m // 경우의 수 증가 + 양쪽 index 변경
                result ++;
                s ++;
                e --;
            }
        }
        
        // 출력
        System.out.println(result);
        br.close();
    }
}