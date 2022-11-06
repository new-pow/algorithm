import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws Exception {
        PriorityQueue<Integer> pq = new PriorityQueue<>((o1, o2) -> {
            if(Math.abs(o1) > Math.abs(o2)) {
                return Math.abs(o1) - Math.abs(o2);
                //절대값 기준으로 두 값이 같다면 음수를 앞으로 보내준다.
            }else if(Math.abs(o1) == Math.abs(o2)) {
                return o1 - o2;
            }else {
                return -1;
            }
        });
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine()); // 연산 개수

        for(int i=0; i<n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x!=0) {
                pq.add(x);
            } else {
                if (pq.isEmpty()) sb.append("0").append("\n");
                else sb.append(pq.poll()).append("\n");
            }
        }
        System.out.println(sb);
    }

}
