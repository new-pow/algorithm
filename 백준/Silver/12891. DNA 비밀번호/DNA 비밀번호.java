import java.io.*;
import java.util.*;

public class Main{
   static int[] acgt;
    static int[] checkAcgt;
    static int check;
    static char[] dnaString;

    public static void main(String[] args) throws Exception{
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken()); // DNA 문자열 길이
        int p = Integer.parseInt(st.nextToken()); // 부분 길이
        int result = 0; // 출력할 값
        checkAcgt = new int[4];
        dnaString = br.readLine().toCharArray();

        st = new StringTokenizer(br.readLine());
        acgt = new int[4];
        for (int i=0; i<4; i++) {
            acgt[i] = Integer.parseInt(st.nextToken()); // A 최소 개수
            if(acgt[i]==0) check ++;
        }

        for (int i=0; i<p; i++) {
            Add(dnaString[i]); // 체크
        }
        if (check==4) result ++;

        // 슬라이딩 윈도우
        for (int i=p; i<s; i++){
            int j=i-p;
            Add(dnaString[i]);
            remove(dnaString[j]);
            if (check==4) result ++;
        }
        System.out.println(result);
        br.close();
    }

    // 문자열 추가
    private static void Add(char c) {
        switch(c) {
            case 'A':
                checkAcgt[0]++;
                if (checkAcgt[0] == acgt[0]) check++;
                break;
            case 'C':
                checkAcgt[1]++;
                if (checkAcgt[1] == acgt[1]) check++;
                break;
            case 'G':
                checkAcgt[2]++;
                if (checkAcgt[2] == acgt[2]) check++;
                break;
            case 'T':
                checkAcgt[3]++;
                if (checkAcgt[3] == acgt[3]) check++;
                break;
        }
    }
    // 문자열 삭제
    private static void remove(char c) {
        switch(c) {
            case 'A':
                if (checkAcgt[0] == acgt[0]) check--;
                checkAcgt[0]--;
                break;
            case 'C':
                if (checkAcgt[1] == acgt[1]) check--;
                checkAcgt[1]--;
                break;
            case 'G':
                if (checkAcgt[2] == acgt[2]) check--;
                checkAcgt[2]--;
                break;
            case 'T':
                if (checkAcgt[3] == acgt[3]) check--;
                checkAcgt[3]--;
                break;
        }
    }
}