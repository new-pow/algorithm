package sec01;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon8979 {

	public static void main(String[] args) throws IOException {
		// 백준 8979 : 올림픽
		// 왜 안 되지?ㅠㅠ 
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken())-1;
		int arr[][] = new int[N][4];
		int rank = 1;
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine()); // st 객체 계속 생성? 
			for(int j = 0; j < 4; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		
		for(int i = 0; i < N; i++) { for(int j = 0; j < 4; j++) {
		System.out.print(arr[i][j] + " "); } System.out.println(); }
		
		for(int i = 0; i < N; i++) {
			System.out.println("aaaaaa");
			if(arr[i][1] > arr[M][1]) {
				rank++;
				System.out.println("g");
			}
			else if(arr[i][1] == arr[M][1] && arr[i][2] > arr[M][2]) {
				rank++;
				System.out.println("s");
			}
			else if(arr[i][1] == arr[M][1] && arr[i][2] == arr[M][2] && arr[i][3] > arr[M][3]) {
				rank++;
				System.out.println("d");
			}
			else {
				System.out.println();
			}
		}
		
		System.out.println(rank);

	}
}
