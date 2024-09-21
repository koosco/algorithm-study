import java.io.*;
import java.util.*;

class Main {

    int[][] dp = new int[1001][3];

    private void sol() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] colors = new int[n+1][3];
        for (int i = 1; i <= n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 3; j++) {
                colors[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        System.arraycopy(colors[1], 0, dp[1], 0, 3);
        for (int i = 2; i < n + 1; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + colors[i][0];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + colors[i][1];
            dp[i][2] = Math.min(dp[i - 1][0], dp[i - 1][1]) + colors[i][2];
        }
        System.out.println(Arrays.stream(dp[n]).min().orElseThrow());
    }

    public static void main(String[] args) throws Exception {
        new Main().sol();
    }
}