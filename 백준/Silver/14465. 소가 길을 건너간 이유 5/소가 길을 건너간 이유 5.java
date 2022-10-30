import java.io.*;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    public static void main(String[] args) throws Exception {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        boolean[] arr = new boolean[N + 1];
        int cnt = 0;
        for (int i = 0; i < B; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num < K + 1) cnt++;
            arr[num] = true;
        }

        int s = 1;
        int e = K;
        int min = K;
        while (e < N) {
            if (!arr[s] && arr[e + 1]) {
                cnt++;
            } else if (arr[s] && !arr[e + 1]) {
                cnt--;
            }
            min = cnt < min ? cnt : min;
            s++;
            e++;
        }
        System.out.println(min);
    }
}