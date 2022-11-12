import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Queue<Integer> arr = new LinkedList<>();

        for (int i=1; i<=n; i++) {
            arr.add(i);
        }

        while (arr.size()!=1) {
            arr.poll();
            arr.add(arr.poll());
        }

        System.out.println(arr.peek());
    }
}