package sec01;

import java.util.*;

public class Sum8393{
    public static void main(String[] args){
        // John got a bad mark in math. The teacher gave him another task.
        // John is to write a program which computes the sum of integers from 1 to n.
        // If he manages to present a correct program, the bad mark will be cancelled.

        // Write a program which:

        // reads the number n from the standard input,
        // computes the sum of integers from 1 to n,
        // writes the answer to the standard output.

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int sum = 0;

//        방법1
//        for(int i=0;i<n+1;i++){sum+=i;}
        
        sum = n*(n+1)/2;
        
        sc.close();

        System.out.println(sum);
    }
}
