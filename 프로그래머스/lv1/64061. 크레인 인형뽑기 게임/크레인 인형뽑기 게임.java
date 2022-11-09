import java.util.*;

class Solution {
        public static int solution(int[][] board, int[] moves) {
        Stack<Integer> basket = new Stack<>();
        int count = 0;

        for (int move : moves) {
            int doll = getDoll(board, move-1, 0);
            if (doll != 0) {
                count = putDoll(basket, doll, count);
            }
        }

        return count;
    }

    public static int getDoll(int[][] board, int move, int deep) {
        int search=0;
        while (search==0) {
            search = board[deep][move];
            if (search!=0) {
                board[deep][move] = 0;
                break;
            } else if (search==0 && deep==board.length-1) {
                break;
            } else if (search==0) {
                deep ++;
            }
        }
        return search;
    }

    public static int putDoll(Stack<Integer> basket, int doll, int count) {
        if (basket.isEmpty()) {
            basket.push(doll);
        } else if (basket.peek()==doll) {
            basket.pop();
            count += 2;
        } else if (basket.peek()!=doll) {
            basket.add(doll);
        }
        return count;
    }
}