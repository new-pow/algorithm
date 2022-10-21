import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n과 m 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // 숫자배열 표그리기
        int[][] nums = new int[n+1][n+1];
        for (int i=1; i<n+1; i++){
            st = new StringTokenizer(br.readLine());
            for (int j=1; j<n+1; j++) nums[i][j] = Integer.parseInt(st.nextToken());
        }
        // 합배열 표 그리기
        int[][] graph = new int[n+1][n+1];
        for (int i=1; i<n+1; i++){
            for (int j=1; j<n+1; j++) graph[i][j] = graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1] + nums[i][j];
        }
        // x1, x2, y1, y2 입력 및 출력
        for (int i=0; i<m; i++){
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            System.out.println(graph[x2][y2]-graph[x2][y1-1]-graph[x1-1][y2]+graph[x1-1][y1-1]);
        }
    }
}