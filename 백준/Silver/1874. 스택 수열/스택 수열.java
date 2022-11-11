import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        int n = sc.nextInt();
        int[] numbers = new int [n];
        for (int i=0; i<n; i++) {
            numbers[i] = sc.nextInt();
        }

        Stack<Integer> stack = new Stack();

        int inputNum = 1;
        boolean result = true;

        for (int i=0; i<numbers.length; i++) {
            int answerNum = numbers[i];
            if (inputNum<=answerNum) {
                while(inputNum<=answerNum) {
                    stack.push(inputNum++);
                    sb.append("+\n");
                }
                stack.pop();
                sb.append("-\n");
            } else {
                int j = stack.pop();
                if (j>answerNum) {
                    System.out.println("NO");
                    result = false;
                    break;
                }
                else {
                    sb.append("-\n");
                }
            }
        }
        if(result) System.out.println(sb.toString());
    }
}