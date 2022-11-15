class Solution {
    public int solution(int price) {
        double discountRate = 0;
        if (price >= 500000) discountRate = 0.2;
        else if (price>= 300000) discountRate = 0.1;
        else if (price >= 100000) discountRate = 0.05;
        return (int)(price - (price*discountRate));
    }
}