import java.io.*;

class Main {

    int[] dp = new int[301];

    private void init_dp(int[] arr) {
        dp[1] = arr[1];
        dp[2] = arr[1] + arr[2];
    }

    private void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] stairs = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            stairs[i] = Integer.parseInt(br.readLine());
        }
        if (n == 1) {
            System.out.println(stairs[1]);
            return;
        }
        init_dp(stairs);

        for (int i = 3; i < n + 1; i++) {
            dp[i] = Math.max(stairs[i - 1] + dp[i - 3], dp[i - 2]) + stairs[i];
        }
        System.out.println(dp[n]);
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}