import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] input = new int[8];
        for (int i=0; i<8; i++){
            input[i] = Integer.parseInt(st.nextToken());
        }
        br.close();
        String result = "";
        for (int i=0; i<input.length-1; i++){
            if (input[i] == input[i+1]-1) {
                result = "ascending";
            } else if (input[i] == input[i+1]+1) {
                result = "descending";
            } else {
                result = "mixed";
                break;
            }
        }
        
        bw.write(result);
        bw.flush();
        bw.close();
    }
}
