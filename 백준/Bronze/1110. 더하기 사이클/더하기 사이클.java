import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        br.close();

        // 변수 정의
        int depth = 0;
        int temp = n;

        // 각자리수 더하기 + 사이클 길이 더하기
        while (true) {
            depth++;
            temp = ((temp%10)*10) + (((temp/10)+(temp%10)) %10);

            if (temp == n) break;
        }
        System.out.println(depth);
    }
}