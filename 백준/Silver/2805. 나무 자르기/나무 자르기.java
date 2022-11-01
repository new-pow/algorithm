import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 나무 수
        int m = Integer.parseInt(st.nextToken()); // 가져갈 나무 길이

        st = new StringTokenizer(br.readLine());
        int[] heights = new int[n]; //
        for (int i=0; i<n; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(heights); // 배열 정렬

        int start = 0; // 시작지점
        int end = heights[heights.length-1]; // 종료지점
        int middle = 0;

        while(start<end){
            long sum = 0;
            middle = (start+end)/2; // 중간지점
            for(int i : heights){
                if (i - middle > 0){
                    sum += (i - middle);
                }
            }

            if (sum < m) {
                end = middle;
            } else {
                start = middle+1;
            }
        }
        System.out.println(start-1);
    }
}