import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i=1; i<n+1; i++) {
            String stars ="";
        for (int j=n-i; j>0; j--) {
            stars += " ";
        }
        for (int j=0; j<i; j++) {
            stars += "*";
        }
        System.out.println(stars);
        }
    }
}