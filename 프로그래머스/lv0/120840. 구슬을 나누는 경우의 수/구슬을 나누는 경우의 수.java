import java.math.BigInteger;

class Solution {
    public BigInteger solution(int balls, int share) {
        BigInteger[] DP = new BigInteger[31];
        DP[0] = new BigInteger("1");
        DP[1] = new BigInteger("1");

        for (int i = 2; i <= 30; i++) {
            DP[i] = DP[i - 1].multiply(new BigInteger(Integer.toString(i)));
        }

        return (DP[balls].divide(DP[balls - share].multiply(DP[share])));

    }
}