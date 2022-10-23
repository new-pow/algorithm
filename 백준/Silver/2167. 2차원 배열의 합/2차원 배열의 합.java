import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
      // 그래프 입력받기 + 합배열 그리기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 세로 크기
        int m = Integer.parseInt(st.nextToken()); // 가로 크기
        int[][] arr = new int[n+1][m+1]; // 합배열
        for (int i=1; i<n+1; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<m+1; j++){
                arr[i][j] = arr[i-1][j]+ arr[i][j-1] - arr[i-1][j-1] + Integer.parseInt(st.nextToken());
            }
        }

        // i, j, x, y 입력받기
        int k = Integer.parseInt(br.readLine());
        for (int a=0; a<k; a++) {
            st = new StringTokenizer(br.readLine());
            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            // 구간합 구하기
            int result = arr[x][y]-arr[i-1][y]-arr[x][j-1]+arr[i-1][j-1];
            System.out.println(result);
        }
    }
}