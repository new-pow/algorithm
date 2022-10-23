import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int s = 1;
        int e = 1;
        int sum = 1;
        int result =1;
        
        while(e!=n){
            if (sum==n){
                e++;
                result ++;
                sum += e;
            } else if (sum>n){
                sum -= s;
                s ++;
            } else{
                e ++;
                sum += e;
            }
        }
        
        System.out.println(result);
    }
}