import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i=1; i<n+1; i++) {
            printStar(i);
        }
    }
    
    static void printStar(int i){
        for (int j=0; j<i; j++) {
            System.out.print('*');
        }
        System.out.println();
    }
}