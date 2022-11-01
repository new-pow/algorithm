// step1. 문제 분석
    // 1. 문자열로 입력 받기
    // 2. 문자 배열로 변환
    // 3. 배열 순서대로 숫자형으로 변환하여 더하기
// step2. 손으로 풀기
// step3. 슈도 코드 작성

// n값 받기

import java.util.*;
import java.io.*;

public class Main { // P11720_숫자의 합
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        // 문자 배열로 변환
        int sum = 0;
        
        for (int i=0; i<N; i++){
            sum += br.read() - '0'; // 정수형으로 변환하면서 sum에 누적
        }
        
        System.out.print(sum);
    }
}