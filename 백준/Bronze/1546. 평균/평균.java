import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        // 과목 개수 n
        int n = sc.nextInt();
        // 성적 저장
        int maxScore = 0;
        int[] scores = new int[n];
        for (int i=0; i<n; i++){
            scores[i] = sc.nextInt();
            if (scores[i] > maxScore) maxScore = scores[i];
        }
        long sum = 0;
        for (int i=0; i<n; i++) {
            long temp = scores[i];
            sum += temp;
        }
        System.out.println(sum*100.0/maxScore/n);
    }
}