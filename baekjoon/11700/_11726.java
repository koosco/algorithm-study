import java.util.*;

class Main {

    int[] dp = new int[1001];

    private void init_dp() {
        dp[1] = 1;
        dp[2] = 2;
        for (int i = 3; i < 1001; i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 10_007;
        }
    }

    private void sol() throws Exception {
        Scanner sc = new Scanner(System.in);
        init_dp();
        int n = sc.nextInt();
        System.out.println(dp[n]);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}