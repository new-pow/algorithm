import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] chess = {1,1,2,2,2,8};
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[6];
        for (int i=0; i<6; i++) {
            arr[i] = chess[i]-Integer.parseInt(st.nextToken());
        }
        for (int i=0; i<5; i++) {
            System.out.print(arr[i]+" ");
        }
        System.out.print(arr[5]);
    }
}