package sec01;

import java.util.*;

public class BruteForce1182 {

	public static void main(String[] args) {
//		N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
//		
//		첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000)
//		둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다.
//		주어지는 정수의 절댓값은 100,000을 넘지 않는다.
//		
//		첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.

		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		if (N<1 || N>20) return;
		
		int S = sc.nextInt();
		if (Math.abs(S) >1000000) return;
		
		System.out.println(N+", "+S);
		
		
		int[] arr = new int[N];
		for (int i=0; i<N; i++) {
			arr[i] = sc.nextInt();
		}
		
		sc.close();
		
		int count = 0;
		
		for (int i=2; i<N; i++) {
			// 부분 수열 경우의 수
			int[] partArr = new int[i];
			for (int j=0; j<i; j++) {
				partArr[j] =
			}
		}
		
		System.out.println(count);
	}

}
